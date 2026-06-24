from fastapi import FastAPI, HTTPException

app = FastAPI()

#simple get endpoint
@app.get("/hello")
def do_hello():
    return {"message": "Hello, World!"}

users = [
    {"id": 1, "name": "Alice"}, 
    {"id": 2, "name": "Bob"},
     {"id": 3, "name": "Charles"}
    ]

#simple get endpoint to return all users
@app.get("/users")
def do_get_all_users():
    return users

#simple get endpoint to return a user by id
@app.get("/users/{user_id}")
def do_get_user(user_id : int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

#For Query Parameters
products = [
    {"id": 1, "name": "Product A", "category": "Electronics", "price": 10.99},
    {"id": 2, "name": "Product B", "category": "Clothing", "price": 19.99},
    {"id": 3, "name": "Product C", "category": "Electronics", "price": 5.99},
    {"id": 4, "name": "Product D", "category": "Clothing", "price": 29.99},
    {"id": 5, "name": "Product E", "category": "Electronics", "price": 15.99}
]

@app.get("/products")
def do_get_products(category: str = None, min_price: float = None, max_price: float = None):
    filtered_products = products

    if category:
        filtered_products = [product for product in filtered_products if product["category"] == category]

    if min_price is not None:
        filtered_products = [product for product in filtered_products if product["price"] >= min_price]

    if max_price is not None:
        filtered_products = [product for product in filtered_products if product["price"] <= max_price]

    return filtered_products