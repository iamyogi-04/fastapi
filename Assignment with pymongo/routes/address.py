from fastapi import APIRouter

from database.db import connection
from models.model import Addresses
from schemas.schema import userAddress, usersAddress
from bson import ObjectId

address = APIRouter()

@address.get('/welcome')
async def main():
    return {"message": "welcome to pymongo"}

@address.get("/")
async def findAddresses():
    return usersAddress(connection.local.user.find())


@address.get("/{id}")
async def one_address(id):
    return userAddress(connection.local.user.find_one({"_id": ObjectId(id)}))

@address.post("/")
async def insert_address(address: Addresses):
    connection.local.user.insert_one(dict(address))
    return usersAddress(connection.local.user.find())


@address.put("/{id}")
async def update_address(id, address: Addresses):
    (connection.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(address)}))
    return userAddress(connection.local.user.find_one({"_id": ObjectId(id)}))


@address.delete("/{id}")
async def delete_address(id):
    return userAddress(connection.local.user.find_one_and_delete({"_id": ObjectId(id)}))
