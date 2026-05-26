from fastapi import APIRouter

from app.schemas.health import HealthRead

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthRead)
async def health_check() -> dict[str, str]:
    """Health check route for confirming the API is running."""
    return {"status": "ok"}
