from fastapi import APIRouter, status

from app.schemas.user import UserCreate, UserRead, UserRole

router = APIRouter(prefix="/auth", tags=["Auth"])

users: list[UserRead] = []


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def register(user_data: UserCreate) -> UserRead:
    """Register a new user."""
    next_id = len(users) + 1

    new_user = UserRead(
        id=next_id,
        email=user_data.email,
        username=user_data.username,
        role=UserRole.USER,
    )

    users.append(new_user)
    return new_user
