import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_establishment():
    establishment_data = {
        "name": "Название места",
        "description": "Описание места",
        "locations": "Место 1, Место 2",
        "opening_hours": "Время работы"
    }
    response = client.post("/establishments/", json=establishment_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Название места"


def test_get_establishments():
    response = client.get("/establishments/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_single_establishment():
    response = client.get("/establishments/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_delete_establishment():
    response = client.delete("/establishments/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Establishment deleted successfully"


def test_create_product():
    product_data = {
        "name": "Новый продукт",
        "description": "Описание продукта",
        "price": 10.99,
        "quantity_in_stock": 100
    }
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Новый продукт"


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_single_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_invalid_route():
    response = client.get("/invalid-route/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"

    