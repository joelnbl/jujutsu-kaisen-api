from typing import TypedDict

from app.schemas.character import CharacterGrade


class Character(TypedDict):
    id: int
    name: str
    grade: CharacterGrade