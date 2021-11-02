from fastapi import APIRouter
from config.db import conn
from models.login import users
from schemas.user import User

login = APIRouter(
    prefix="/login",
)

@login.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@login.post("/users")
def create_user(user: User):
    new_user = user.dict()
    result = conn.execute(users.insert().values(new_user))
    print (result)
    return user