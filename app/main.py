from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(
    title="Jujutsu Kaisen API",
    description="REST API for Jujutsu Kaisen characters, techniques, users, and auth.",
    version="0.1.0",
  )

app.include_router(api_router, prefix="/api/v1")


@app.get("/", include_in_schema=False)
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Jujutsu Kaisen API"}