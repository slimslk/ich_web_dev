import logging
from sqlalchemy.orm import sessionmaker

from homework.hw_3 import engine, models
from homework.hw_3.models import Category, Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("sqlalchemy.engine")
logger.setLevel(logging.INFO)

models.main()

Session = sessionmaker(bind=engine)
session = Session()

game_category = Category(
    name="Games",
    description="Video games"
)

toy_category = Category(
    name="Toys",
    description="Kids toys"
)

session.add(game_category)
session.add(toy_category)

product_1 = Product(
    name="Arcanum",
    price=10.99,
    in_stock=True,
    category_id=1
)

product_2 = Product(
    name="Gummy Duck",
    price=3.99,
    in_stock=True,
    category_id=2
)

session.add(product_1)
session.add(product_2)
session.commit()

category = session.query(Category).filter(Category.id == 1).first()

session.delete(category)
session.commit()

categories = session.query(Category).all()
products = session.query(Product).all()

for ct in categories:
    print(f"name={ct.name}", ct.id)

for pr in products:
    print(f"prod_name={pr.name}")

session.close()
