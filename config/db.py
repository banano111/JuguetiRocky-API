from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:urbano111@localhost:3306/test_api")

meta = MetaData()

conn = engine.connect()