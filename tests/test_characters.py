from fastapi.testclient import TestClient

from app.main import app
from app.schemas.character import CharacterGrade

client = TestClient(app)


def test_list_characters() -> None:
    response = client.get("/api/v1/characters")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Yuji Itadori", "grade": CharacterGrade.FIRST_YEAR},
        {"id": 2, "name": "Satoru Gojo", "grade": CharacterGrade.SPECIAL_GRADE},
        {"id": 3, "name": "Nobara Kugisaki", "grade": CharacterGrade.FIRST_YEAR},
    ]


def test_get_character_by_id_returns_character() -> None:
    response = client.get("/api/v1/characters/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Yuji Itadori", "grade": CharacterGrade.FIRST_YEAR}


def test_get_character_by_unknown_id_returns_404() -> None:
    response = client.get("/api/v1/characters/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Character not found"}


def test_list_characters_can_filter_by_grade() -> None:
    response = client.get("/api/v1/characters?grade=First-year")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Yuji Itadori", "grade": CharacterGrade.FIRST_YEAR},
        {"id": 3, "name": "Nobara Kugisaki", "grade": CharacterGrade.FIRST_YEAR},
    ]


def test_list_characters_with_invalid_grade_returns_422() -> None:
    response = client.get("/api/v1/characters?grade=Unknown")

    assert response.status_code == 422