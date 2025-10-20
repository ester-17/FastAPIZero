from fastapi import FastAPI

from fastapi_zero.schemas import Message, UserSchema

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}

@app.post('/user/')
def create_user(user: UserSchema):
    ...