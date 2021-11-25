from fastapi import APIRouter
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from config.db import conn
from models.products import productos


products = APIRouter(
    prefix="/products",
)

@products.get("/")
def most_wanted():
    all_products = conn.execute(productos.select()).all()
    return all_products

@products.get("/mostwanted")
def most_wanted():
    products_mostwanted = conn.execute(productos.select().where(productos.c.MostWanted == 1)).all()
    return products_mostwanted

@products.get("/{product_id}")
def ind_product(product_id):
    print(product_id)
    product = conn.execute(productos.select().where(productos.c.id_producto == product_id)).first()
    return product