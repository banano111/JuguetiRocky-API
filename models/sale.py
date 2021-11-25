from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR, String, SmallInteger, VARBINARY
from config.db import meta, engine
from models.login import users

sale = Table("sale", meta, 
    Column("sale_id", SmallInteger, primary_key=True), 
    Column("user_id", SmallInteger, ForeignKey("users.id")),
    Column("total_sale", SmallInteger),
    Column("ship_status", VARCHAR(15)),
    )
