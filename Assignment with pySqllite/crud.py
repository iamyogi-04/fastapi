from fastapi import Depends, FastAPI, status, Response
import schema
import model
from db import SessionLocal, engine
from sqlalchemy.orm import Session
from getcoordinate import getcoordinate
from geopy.distance import geodesic

app = FastAPI()

model.Base.metadata.create_all(engine)

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def main():
    return {"message": "welcome to addressbook"}        

# creating address frombody 

@app.post("/createAddress", status_code=status.HTTP_201_CREATED)
def create_address(req: schema.Address, res:Response, db :Session = Depends(getDb)):
    try:
        # removing leading and ending extra space 
        addressLine = req.addressLine.strip()
        city = req.city.strip()
        state = req.state.strip()
        postalCode = req.postalCode

        # getting the location & coordinate data from mapquest api 
        locationData = getcoordinate(addressLine, city, state)

        # creaing row for address 
        newAddress = model.Address(
            addressLine = addressLine,
            city = city,
            state = state,
            country = locationData,
            postalCode = postalCode,
            longitude =  locationData,
            latitude =  locationData,
            mapUrl = locationData
        )

        # adding row to tabel
        db.add(newAddress)
        db.commit()
        db.refresh(newAddress)

        return {
            "status": "sucessfullycomplete",
            "data": newAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status" : "failed to create",
            "msg" : str(e)
        }


# get all the address 

@app.get("/readAllAddress", status_code=status.HTTP_200_OK)
def get_all_address(res: Response, db :Session = Depends(getDb)):
    try:
        # get all the address data from  database and send to user 
        allAddress = db.query(model.Address).all()
        return{
            "status" :"completed",
            "data" : allAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR 
        return {
            "status" : "failed to load",
            "msg" : str(e)
        }



# update the address through id and request body 

@app.put("/updateAddress/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_address(id, req: schema.Address, res: Response, db: Session = Depends(getDb)):
    try:
        # removing leading and ending extra space 
        addressLine = req.addressLine.strip()
        city = req.city.strip()
        state = req.state.strip()
        postalCode = req.postalCode

        # getting the location & coordinate data from mapquest api 
        locationData = getcoordinate(addressLine, city, state)

        newAddress = {
            "addressLine" : addressLine,
            "city" : city,
            "state" : state,
            "country" : locationData,
            "postalCode" : postalCode,
            "longitude" :  locationData,
            "latitude" :  locationData,
            "mapUrl" : locationData
        }

        # updating address through id and query params 
        updatedAddress = db.query(model.Address).filter(model.Address.id == id).update(newAddress)

        # if data not found in database 
        if not updatedAddress:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status" : "failed to find data",
                "msg" : f"Address id {id} not found"
            }

        db.commit()

        # if data got sucessfully updated 
        return {
            "status" : "ok",
            "data" : updatedAddress
        }
    
    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status" : "failed to update Address",
            "msg" : str(e)
        }


# delete the address through id 

@app.delete("/deleteAddress/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_address(id, res: Response, db: Session = Depends(getDb) ):
    try:
        # deleting address from databse through id
        deletedAddress = db.query(model.Address).filter(model.Address.id == id).delete(synchronize_session=False)

        # if data not found in database 
        if not deletedAddress:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status" : "failed to delete address",
                "msg" : f"Address id {id} not found"
            }
        
        db.commit()

        # if data got sucessfully deleted 
        return {
            "status" : "ok",
            "data" : deletedAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status" : "failed",
            "msg" : str(e)
        }