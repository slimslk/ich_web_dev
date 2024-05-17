from sqlalchemy import func

from homework.hw_4 import engine, test_data, models
from homework.hw_4.connector import DBConnector
from homework.hw_4.models import Product, Category

YELLOW = "\033[93m"
RESET = "\033[0m"

with (DBConnector(engine) as session):
    models.create_entities()
    test_data.add_fake_data()

    # 2. Извлеките все записи из таблицы categories. Для каждой категории извлеките и выведите
    # все связанные с ней продукты, включая их названия и цены.
    print(f"{YELLOW}Task2{RESET}")
    categories: list[Category] = session.query(Category).all()

    for category in categories:
        products: list[Product] = session.query(Product).filter(Product.category_id == category.id).all()

        if products:
            print(f"Category: {category.name}")
            for product in products:
                print(f"{product.name:<30} | price: {product.price:<7} | in stock: {"Yes" if product.in_stock else "No"}")
            print("^"*50)


    # 3. Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.
    print(f"{YELLOW}Task3{RESET}")
    product: Product = session.query(Product).filter(Product.name == "Смартфон").one_or_none()
    if product:
        product.price = 349.99
        session.commit()

    new_product: Product = session.query(Product).filter(Product.name == "Смартфон").one_or_none()
    print(f"{new_product.name} | {new_product.price}")
    print("^" * 50)

    # 4. Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.
    print(f"{YELLOW}Task4{RESET}")
    products_in_category: list[Product] = session.query(Product, func.count(Product.id)
                                                        .label("amount_of_products")).group_by(Product.category_id)

    for product in products_in_category:
        print(f"Category: {product.Product.category.name:<13} | amount of products: {product.amount_of_products}")
    print("^" * 50)

    # 5. Отфильтруйте и выведите только те категории, в которых более одного продукта.
    print(f"{YELLOW}Task5{RESET}")
    categories_more_one_item: list[Product] = session.query(
        Product
    ).group_by(Product.category_id).having(func.count(Product.id) > 1).all()

    if categories_more_one_item:
        for product in categories_more_one_item:
            print(f"Category name: {product.category.name}")
