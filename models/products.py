from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import VARCHAR, String, SmallInteger
from config.db import meta, engine

productos = Table("productos", meta, 
    Column("id_producto", SmallInteger, primary_key=True), 
    Column("Nombre", VARCHAR(30)),
    Column("CostoProducto", SmallInteger),
    Column("Stock", SmallInteger),
    Column("Categoria", VARCHAR(30)),
    Column("Descripcion", VARCHAR(100)),
    Column("Imagen", VARCHAR(500)),
    Column("MostWanted", SmallInteger)
    )
