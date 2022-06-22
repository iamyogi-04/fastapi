from fastapi import FastAPI

app = FastAPI(
    title="AdressBook",
    description="get adress information"
)

@app.get('/')
async def crud():
    return {"message":"hello yogi "}

    