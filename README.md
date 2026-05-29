# Jujutsu Kaisen API

<p align="center">
  <img src="https://media.giphy.com/media/orvJf7kwgc2iakssc4/giphy.gif" width="520" alt="Jujutsu Kaisen Gojo GIF" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue" alt="Python 3.14" />
  <img src="https://img.shields.io/badge/FastAPI-0.136.3-009688" alt="FastAPI" />
  <img src="https://img.shields.io/badge/tests-pytest-green" alt="pytest" />
  <img src="https://img.shields.io/badge/license-MIT-black" alt="MIT License" />
</p>

A learning-focused REST API inspired by Jujutsu Kaisen, built with FastAPI while practicing clean project structure, schemas, enums, validation, and TDD.

## Features

- Versioned API under `/api/v1`
- Character listing endpoint
- Character detail endpoint
- Admin character creation endpoint
- Grade filtering with enum validation
- User registration endpoint
- Health check endpoint
- Pydantic response schemas
- Pytest coverage for the current API behavior
- Clean package structure ready to grow into auth, users, and more resources

## Tech Stack

- FastAPI
- Pydantic
- Pytest
- Python virtual environments

## Project Structure

```text
app/
  api/
    v1/
      endpoints/
        auth.py
        characters.py
        health.py
      router.py
  schemas/
    auth.py
    character.py
    health.py
    user.py
  main.py
tests/
  test_auth.py
  test_characters.py
  test_health.py
```

## Getting Started

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the development server:

```bash
fastapi dev
```

Open the API docs:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/health` | Check API status |
| `GET` | `/api/v1/characters` | List all characters |
| `GET` | `/api/v1/characters?grade=First-year` | Filter characters by grade |
| `GET` | `/api/v1/characters/{character_id}` | Get one character by ID |
| `POST` | `/api/v1/admin/characters` | Create a new character as an admin action |
| `POST` | `/api/v1/auth/register` | Register a new user |

## Business Logic

The public character routes behave like a read-only catalog. Anyone can browse,
filter, and inspect characters.

Catalog writes are separated under admin routes:

```text
/api/v1/admin/characters
```

User registration is currently implemented in memory. New users are assigned the
`user` role by the backend, and passwords are accepted only as input data: they
are not returned in API responses.

Login, password hashing, JWT sessions, and real role-based authorization are not
implemented yet. The API structure already reflects the intended product rule:
normal users should not create official catalog characters.

## Example Responses

List characters:

```json
[
  {
    "id": 1,
    "name": "Yuji Itadori",
    "grade": "First-year"
  },
  {
    "id": 2,
    "name": "Satoru Gojo",
    "grade": "Special grade"
  }
]
```

Health check:

```json
{
  "status": "ok"
}
```

Create character:

```http
POST /api/v1/admin/characters
Content-Type: application/json
```

```json
{
  "name": "Maki Zenin",
  "grade": "First-year"
}
```

Expected response:

```json
{
  "id": 4,
  "name": "Maki Zenin",
  "grade": "First-year"
}
```

Register user:

```http
POST /api/v1/auth/register
Content-Type: application/json
```

```json
{
  "email": "yuji@example.com",
  "username": "yuji",
  "password": "secret123"
}
```

Expected response:

```json
{
  "id": 1,
  "email": "yuji@example.com",
  "username": "yuji",
  "role": "user"
}
```

## Validation

The `grade` query parameter is backed by an enum, so invalid values return `422`.

Valid values:

```text
First-year
Special grade
```

Example invalid request:

```text
GET /api/v1/characters?grade=Unknown
```

Expected status:

```text
422 Unprocessable Entity
```

## Running Tests

```bash
python -m pytest
```

Current test coverage focuses on:

- Listing characters
- Getting a character by ID
- Returning `404` when a character does not exist
- Filtering by grade
- Rejecting invalid grade filters
- Creating characters through the admin route
- Rejecting character creation on the public catalog route
- Registering users without returning passwords
- Health check response

## Roadmap

- Add persistent database storage
- Add login
- Add password hashing
- Add JWT authentication
- Add forgot password and reset password flow
- Enforce admin-only create/update/delete endpoints with authentication
- Add more Jujutsu Kaisen resources such as techniques, clans, and domains

## License

This project is licensed under the MIT License.
