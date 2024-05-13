from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey, String

from homework.hw_3 import Base, engine


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, default=0.0)
    in_stock = Column(Boolean, default=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))


def main():
    Base.metadata.create_all(bind=engine)
