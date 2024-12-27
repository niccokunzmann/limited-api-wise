"""Test the main API."""


def test_read_main(api):
    response = api.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
