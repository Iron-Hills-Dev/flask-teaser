from app import app


def test_should_respond_correctly(mocker):
    mocker.patch('domain.date.month_service.get_days_left', return_value=5)

    # given
    app.config.update({"TESTING": True})
    _client = app.test_client()

    # when
    _request = _client.get("/month/days-left", headers={"Accept": "application/json"})

    # then
    assert _request.status_code == 200
    assert _request.json == {"daysLeft": 5}


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
