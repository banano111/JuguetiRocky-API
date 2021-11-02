from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import VARCHAR, String, SmallInteger
from config.db import meta, engine

users = Table("users", meta, 
    Column("id", SmallInteger, primary_key=True), 
    Column("name", VARCHAR(20)),
    Column("last_name", VARCHAR(20)),
    Column("email", VARCHAR(30)),
    Column("password", VARCHAR(100))
    )
