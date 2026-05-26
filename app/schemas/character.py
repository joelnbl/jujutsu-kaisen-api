from enum import StrEnum

from pydantic import BaseModel


class CharacterGrade(StrEnum):
    FIRST_YEAR = "First-year"
    SPECIAL_GRADE = "Special grade"


class CharacterRead(BaseModel):
    id: int
    name: str
    grade: CharacterGrade

