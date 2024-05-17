from homework.hw_4 import engine
from homework.hw_4.connector import DBConnector
from homework.hw_4.models import Category, Product


def add_fake_data():
    with DBConnector(engine) as session:
        categories = [
            Category(
                name="Электроника",
                description="Гаджеты и устройства."
            ),
            Category(
                name="Книги",
                description="Печатные книги и электронные книги."
            ),
            Category(
                name="Одежда",
                description="Одежда для мужчин и женщин."
            )

        ]
        session.add_all(categories)
        session.commit()

        products = [
            Product(
                name="Смартфон",
                price=299.99,
                in_stock=True,
                category_id=1
            ),
            Product(
                name="Ноутбук",
                price=499.99,
                in_stock=True,
                category_id=1
            ),
            Product(
                name="Научно-фантастический роман",
                price=15.99,
                in_stock=True,
                category_id=2
            ),
            Product(
                name="Джинсы",
                price=40.50,
                in_stock=True,
                category_id=3
            ),
            Product(
                name="Футболка",
                price=20.00,
                in_stock=True,
                category_id=3
            )
        ]
        session.add_all(products)
        session.commit()