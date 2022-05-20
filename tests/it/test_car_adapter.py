import logging
import uuid


def test_add_car(client):
    # when
    _req = client.post("/car", json={"model": "Lamborghini Hurracan", "regNum": "EPA1234"},
                       headers={"Accept": "application/json", "Content-Type": "application/json"})

    # then
    logging.error(_req.data)
    assert _req.status_code == 200
    assert isinstance(_req.json["id"], str)


def test_find_car(client):
    # when
    _req = client.get("/car/1febc510-cc5f-11ec-9d64-0242ac120002")

    # then
    assert _req.status_code == 200
    assert _req.json["id"] == "1febc510-cc5f-11ec-9d64-0242ac120002"
    assert _req.json["model"] == "Porsche Cayenne"
    assert _req.json["regNum"] == "XX 1234"


def test_delete_car(client):
    # when
    _req = client.delete("/car/1febc510-cc5f-11ec-9d64-0242ac120002")

    # then
    assert _req.status_code == 204
