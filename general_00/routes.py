from fastapi import APIRouter, HTTPException
from general_00.general_methods import add_patient, add_product, get_all_users, get_products, hello
from general_00.model.patient import Patient

router = APIRouter()

#simple get endpoint
@router.get("/hello")
def do_hello():
    return hello()

#simple get endpoint to return all users
@router.get("/users")
def do_get_all_users():
    return get_all_users()

@router.get("/products")
def do_get_products(category: str = None, min_price: float = None, max_price: float = None):
    return get_products(category,min_price, max_price)

@router.post("/products")
def do_add_product(product: dict):
    return add_product(product)

@router.post("/patient")
def do_add_patient(patient: Patient):
    patient.weight = 2000.002
    return add_patient(patient)