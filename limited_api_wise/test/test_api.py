"""Test the main API."""


def test_check_settings(api):
    response = api.get("/settings.json")
    assert response.status_code == 200
    r = response.json()
    assert r["license"] == "AGPL-3.0"
    assert r["environment"] == "sandbox"
    assert not any("token" in k.lower() for k in r.keys())


def test_settings_show_version(api):
    """We want to know what code we are running."""
    from limited_api_wise import __version__, __version_tuple__

    response = api.get("/settings.json")
    assert response.status_code == 200
    r = response.json()
    assert r["version"] == {
        "text": __version__,
        "list": list(__version_tuple__),
        "source": "https://github.com/niccokunzmann/limited-api-wise",
    }
