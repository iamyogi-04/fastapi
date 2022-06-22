from fastapi import FastAPI
from routes.address import address
app= FastAPI(
    title="AddressBook",
    description=" AddressBook using pymongo"
)
app.include_router(address)