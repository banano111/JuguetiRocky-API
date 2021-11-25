from fastapi import APIRouter
from config.db import conn
from models.sale import sale as sale_db
from schemas.sales import Sale

sales = APIRouter(
    prefix="/sales",
)

@sales.post("/new_sale")
def create_sale(sale: Sale):
    new_sale = sale.dict()
    result = conn.execute(sale_db.insert().values(new_sale))
    
    print(result)

    return {"sale_created": True}

@sales.get("/user/{user_id}")
def get_user_sales(user_id):
    print(user_id)
    user_sales = conn.execute(sale_db.select().where(sale_db.c.user_id == user_id)).all()
    return user_sales