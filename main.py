from fastapi import FastAPI
from router.api import router as api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def read_root():
    return{"message": "Hello world!"}
