from general_00.model.patient import Patient
from general_00.static_data import ProductRepo


def hello():
    return {"message": "Hello, World!"}


def get_all_users():
    return ProductRepo.users

def get_products(category: str = None, min_price: float = None, max_price: float = None):
    filtered_products = ProductRepo.products

    if category:
        filtered_products = [product for product in filtered_products if product["category"] == category]

    if min_price is not None:
        filtered_products = [product for product in filtered_products if product["price"] >= min_price]

    if max_price is not None:
        filtered_products = [product for product in filtered_products if product["price"] <= max_price]

    return filtered_products

def add_product(product: dict):
    product_id = len(ProductRepo.products) + 1
    product["id"] = product_id
    ProductRepo.products.append(product)
    return ProductRepo.products

def add_patient(patient: Patient):
    return patient