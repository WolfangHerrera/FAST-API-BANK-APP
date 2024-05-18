from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from app.routers import customer
from app.core.config import settings
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"Detail": 'Bad request or resource does not exist.'}
    )


client = AsyncIOMotorClient(settings.mongo_uri)
db = client.mydatabase

app.include_router(customer.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
