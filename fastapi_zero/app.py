from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    """Seleciona todos os campos de user e passa chave e valor para UserDB,
    para transformar o objeto do pydantic em dicionário"""
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)

    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"users": database}
