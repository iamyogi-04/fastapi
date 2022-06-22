from pydantic import BaseModel

class Addresses(BaseModel):
    address: str
    city: str
    state:str
    pincode:int
    country:str

