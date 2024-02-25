from app.routers import products, establishments

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(products.router)
api_router.include_router(establishments.router)
