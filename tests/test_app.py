from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Act (ação): chama a função com o endpoint '/'

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(  # UserSchema
        "/user/",
        json={
            "username": "abacaxi",
            "password": "password",
            "email": "abacaxi@test.com",
        },
    )
    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED

    # Valida UserPublic
    assert response.json() == {
        "username": "abacaxi",
        "email": "abacaxi@test.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status.code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testusername",
                "email": "test@test.com",
                "id": 1,
            }
        ]
    }
