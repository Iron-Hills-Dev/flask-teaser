from datetime import date

from app import app
from domain.date import month_service


def test_should_respond_correctly():
    # given
    app.config.update({"TESTING": True})
    _client = app.test_client()

    # when
    _request = _client.get("/month/days-left", headers={"Accept": "application/json"})

    # then
    assert _request.status_code == 200
    assert _request.json == {"daysLeft": month_service.get_days_left(date.today())}


def test_bad_accept_header():
    # given
    app.config.update({"TESTING": True})
    _client = app.test_client()

    # when
    _request = _client.get("/month/days-left", headers={"Accept": "plain/text"})

    # then
    assert _request.status_code == 406
    assert _request.json == {"error": 1, "desc": "Wrong 'Accept' header"}


def test_no_accept_header():
    # given
    app.config.update({"TESTING": True})
    _client = app.test_client()

    # when
    _request = _client.get("/month/days-left", headers={})

    # then
    assert _request.status_code == 406
    assert _request.json == {"error": 2, "desc": "No 'Accept' header given"}