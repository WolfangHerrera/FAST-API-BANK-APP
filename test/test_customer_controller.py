from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_customer():
    customer_data = {
        "name": "Wolfang",
        "last_name": "Herrera",
        "dni": 0
    }

    response = client.post("/accounts/", json=customer_data)
    assert response.status_code == 200
    assert response.json()["account_id"] == "0"
