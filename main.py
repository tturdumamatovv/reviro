from fastapi import FastAPI

from app.routers.api import api_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Inventory Management System!"}


app.include_router(api_router)

