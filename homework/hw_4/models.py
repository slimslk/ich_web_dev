from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from homework.hw_4 import Base, engine


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, default=0.0)
    in_stock = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))

    category = relationship("Category")


def create_entities():
    Base.metadata.create_all(bind=engine)