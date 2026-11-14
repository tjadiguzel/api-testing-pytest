import httpx
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def client():
    with httpx.Client(base_url=BASE_URL, timeout=30) as c:
        yield c


@pytest.fixture(scope="session")
def token(client):
    response = client.post(
        "/auth", json={"username": "admin", "password": "password123"}
    )
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Tulay",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-12-01", "checkout": "2026-12-05"},
        "additionalneeds": "Breakfast",
    }
