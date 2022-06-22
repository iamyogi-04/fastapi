from pydantic import BaseModel

# using pydantic BaseModel creating an request model (schema)


class Address(BaseModel):
    addressLine: str 
    city: str 
    state: str
    postalCode: int