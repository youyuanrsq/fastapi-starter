from fastapi import APIRouter
import src.auth.router as auth

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])
