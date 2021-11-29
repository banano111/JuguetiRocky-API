from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.login import login
from routes.products import products
from routes.sales import sales

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://main.d3s6akcfwgatsl.amplifyapp.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login)
app.include_router(products)
app.include_router(sales)