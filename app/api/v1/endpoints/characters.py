from fastapi import APIRouter, HTTPException, status

from app.schemas.character import CharacterCreate, CharacterGrade, CharacterRead
from app.types.character import Character

router = APIRouter(prefix="/characters", tags=["Characters"])
admin_router = APIRouter(prefix="/admin/characters", tags=["Admin Characters"])

characters: list[Character] = [
    {"id": 1, "name": "Yuji Itadori", "grade": CharacterGrade.FIRST_YEAR},
    {"id": 2, "name": "Satoru Gojo", "grade": CharacterGrade.SPECIAL_GRADE},
    {"id": 3, "name": "Nobara Kugisaki", "grade": CharacterGrade.FIRST_YEAR},
]


@router.get("", response_model=list[CharacterRead])
async def list_characters(grade: CharacterGrade | None = None) -> list[Character]:
    """Endpoint to list characters."""
    if grade is None:
        return characters

    return [
        character
        for character in characters
        if character["grade"].lower() == grade.lower()
    ]


@router.get("/{character_id}", response_model=CharacterRead)
async def get_character(character_id: int) -> Character:
    """Endpoint to get character by ID."""
    for character in characters:
        if character["id"] == character_id:
            return character
    raise HTTPException(status_code=404, detail="Character not found")


@admin_router.post(
    "",
    response_model=CharacterRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_character(character_data: CharacterCreate) -> Character:
    """Endpoint to create character."""
    next_id = max(character["id"] for character in characters) + 1
    new_character: Character = {
        "id": next_id,
        "name": character_data.name,
        "grade": character_data.grade,
    }

    characters.append(new_character)
    return new_character
