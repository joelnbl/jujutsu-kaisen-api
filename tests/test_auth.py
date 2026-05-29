from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_user_returns_created_user() -> None:
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "yuji@example.com",
            "username": "yuji",
            "password": "secret123",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "email": "yuji@example.com",
        "username": "yuji",
        "role": "user",
    }
