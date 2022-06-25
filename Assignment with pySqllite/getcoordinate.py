import requests
# using mapquest api for getting the coordinate for particular address
# my secret key
coordinateSecretKey = "BnauYX5SgIrwS7FSLr3rCbgGPct3DLaa"

# api end-point with querylocation using f-strings
coordinateApi = f"http://www.mapquestapi.com/geocoding/v1/address?key={coordinateSecretKey}&location="


# getting the  address information along with coordinate of an address 

def getcoordinate(addressLine, city, state):  #takes 3 parameters for using as location query
    mainCoordinateApi = f"{coordinateApi}{addressLine},{city},{state}"
    r = requests.get(mainCoordinateApi)
    locationData = r.json()["results"][0]["locations"][0]
    print(locationData)
    return locationData


