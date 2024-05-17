from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

sql_config = f"sqlite:///:memory:"
engine = create_engine(sql_config)

Base = declarative_base()
