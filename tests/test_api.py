def test_root_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

def test_get_products(client):
    response = client.get("/api/products/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_product(client):
    product_data = {
        "name": "Test Headphones",
        "description": "Test product for automated testing",
        "price": "999.99",
        "stock_quantity": 10,
        "category_id": None,
        "image_url": None,
    }

    create_response = client.post(
        "/api/products/",
        json=product_data,
    )

    assert create_response.status_code == 201

    product_id = create_response.json()["id"]

    response = client.get(f"/api/products/{product_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "Test Headphones"


def test_get_nonexistent_product(client):
    response = client.get("/api/products/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

def test_soft_delete_product(client):
    product_data = {
        "name": "Product To Delete",
        "description": "Testing soft deletion",
        "price": "499.99",
        "stock_quantity": 5,
        "category_id": None,
        "image_url": None,
    }

    create_response = client.post(
        "/api/products/",
        json=product_data,
    )

    assert create_response.status_code == 201

    product_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/api/products/{product_id}"
    )

    assert delete_response.status_code == 204

    get_response = client.get(
        f"/api/products/{product_id}"
    )

    assert get_response.status_code == 404

def test_get_categories(client):
    response = client.get("/api/categories/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_category(client):
    category_data = {
        "name": "Accessories",
        "description": "Retail accessories",
    }

    response = client.post(
        "/api/categories/",
        json=category_data,
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Accessories"
    assert response.json()["description"] == "Retail accessories"
    assert "id" in response.json()

def test_create_duplicate_category(client):
    category_data = {
        "name": "Electronics",
        "description": "Electronic products",
    }

    first_response = client.post(
        "/api/categories/",
        json=category_data,
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/api/categories/",
        json=category_data,
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == (
        "A category with this name already exists"
    )
