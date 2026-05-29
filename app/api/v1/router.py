from fastapi import APIRouter

from app.api.v1.endpoints import auth, characters, health

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(health.router)
api_router.include_router(characters.router)
api_router.include_router(characters.admin_router)
