from fastapi import FastAPI
from app.auth.routers import router as auth_router

app = FastAPI()

app.include_router(
    auth_router,
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

