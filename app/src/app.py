from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router, tags=["Event"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
