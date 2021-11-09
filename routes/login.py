from os import environ as env
from dotenv import load_dotenv

from fastapi import APIRouter
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from config.db import conn
from models.login import users
from schemas.user import User, User_Auth

from cryptography.fernet import Fernet

load_dotenv()

f = Fernet(env["KEY"].encode("utf-8"))

login = APIRouter(
    prefix="/login",
)

@login.post("/auth")
def authentication(user_to_auth: User_Auth):
    
    print(f'Peticion para login del usuario {user_to_auth.email}')

    user_db = conn.execute(users.select().where(users.c.email == user_to_auth.email)).first()
    
    if user_db is None:
        return {
            "is_auth": False,
            "error": "No User Found"
            }
    else:
        decrypt_pass = f.decrypt(user_db["password"])
    
    if user_to_auth.password == decrypt_pass.decode():
        user_auth = {
            "name": user_db["name"],
            "last_name": user_db["last_name"],
            "email": user_db["email"],
            "is_auth": True
        }
        print(f'Usuario {user_auth["email"]} logeado con exito')
        return user_auth
    else:
        print(f'Usuario {user_to_auth.email} error al inicio de sesion')
        return {"is_auth" : False}

@login.post("/register")
def create_user(user: User):
    new_user = user.dict()
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    
    print(result)

    return {"user_created": True}