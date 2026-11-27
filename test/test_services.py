import pytest

from app.services import (
    get_all_services,
    get_service,
    register_service,
    validate_service,
)


def test_register_service_adds_service_with_unknown_status():
    services = []

    service = register_service("api", "https://api.example.com", services)

    assert service == {
        "name": "api",
        "url": "https://api.example.com",
        "status": "unknown",
    }
    assert services == [service]


def test_register_service_accepts_http_url():
    services = []

    service = register_service("web", "http://localhost:8080", services)

    assert service["url"] == "http://localhost:8080"
    assert get_service("web", services) is service


def test_register_service_rejects_duplicate_name():
    services = []
    register_service("api", "https://api.example.com", services)

    with pytest.raises(ValueError, match="Service already exists"):
        register_service("api", "https://other.example.com", services)

    assert len(services) == 1


@pytest.mark.parametrize("name", ["", "   ", None])
def test_validate_service_rejects_invalid_name(name):
    with pytest.raises(ValueError, match="Invalid service name"):
        validate_service(name, "https://api.example.com")


@pytest.mark.parametrize("url", ["", "   ", None, "ftp://api.example.com", "https://"])
def test_validate_service_rejects_invalid_url(url):
    with pytest.raises(ValueError, match="Invalid service URL"):
        validate_service("api", url)


@pytest.mark.parametrize("url", ["http://api.example.com", "https://api.example.com/path"])
def test_validate_service_accepts_valid_url(url):
    validate_service("api", url)


def test_get_service_returns_none_when_not_found():
    services = []

    assert get_service("missing", services) is None


def test_get_all_services_returns_registered_services():
    services = []
    first = register_service("api", "https://api.example.com", services)
    second = register_service("web", "https://web.example.com", services)

    assert get_all_services(services) == [first, second]
