from typing import Optional
from fastapi import APIRouter
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import user
from config.db import conn
from models.products import productos


products = APIRouter(
    prefix="/products",
)

@products.get("/")
def get_products(categoria: Optional[str] = None, marca: Optional[str] = None):
    if categoria:
        category_products = conn.execute(productos.select().where(productos.c.Categoria == categoria)).all()
        return category_products
    elif marca:
        brand_products = conn.execute(productos.select().where(productos.c.Marca == marca)).all()
        return brand_products
    else:
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