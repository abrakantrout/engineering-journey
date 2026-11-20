import pytest

from fastapi.testclient import TestClient
from authentication import app, users

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_users():
    users.clear()
    yield
    users.clear()


def test_user_registration():
    response = client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"


def test_duplicate_registration():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }

    client.post("/register", json=user_data)
    response = client.post("/register", json=user_data)

    assert response.status_code == 400


def test_user_login():
    client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_protected_profile():
    client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/profile",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200