from fastapi import FastAPI

from routes.login import login

app = FastAPI()

app.include_router(login)