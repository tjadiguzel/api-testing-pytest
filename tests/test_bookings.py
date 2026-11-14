def test_health_check(client):
    response = client.get("/ping")
    assert response.status_code == 201


def test_list_bookings_returns_ids(client):
    response = client.get("/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "bookingid" in response.json()[0]


def test_create_and_get_booking(client, booking_payload):
    created = client.post("/booking", json=booking_payload)
    assert created.status_code == 200
    booking_id = created.json()["bookingid"]

    fetched = client.get(f"/booking/{booking_id}")
    assert fetched.status_code == 200
    assert fetched.json()["firstname"] == "Tulay"
    assert fetched.json()["totalprice"] == 150


def test_delete_booking(client, token, booking_payload):
    booking_id = client.post("/booking", json=booking_payload).json()["bookingid"]

    deleted = client.delete(f"/booking/{booking_id}", headers={"Cookie": f"token={token}"})
    assert deleted.status_code == 201

    assert client.get(f"/booking/{booking_id}").status_code == 404


def test_delete_without_token_is_rejected(client, booking_payload):
    booking_id = client.post("/booking", json=booking_payload).json()["bookingid"]

    response = client.delete(f"/booking/{booking_id}")
    assert response.status_code == 403
