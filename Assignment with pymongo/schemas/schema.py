def userAddress(item) -> dict:
    return{
        "id": str(item["_id"]),
        "address": item["address"],
        "city": item["city"],
        "state": item["state"],
        "pincode": item["pincode"],
        "country": item["country"],
    }

def usersAddress(entity) -> list:
    return [userAddress(item) for item in entity]