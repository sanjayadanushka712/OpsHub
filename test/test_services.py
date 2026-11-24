import pytest

from app.services import register_service


def test_register_service():
    result = register_service(
        "Payment API",
        "https://example.com"
    )

    assert result["name"] == "Payment API"
    assert result["url"] == "https://example.com"
    assert result["status"] == "unknown"


def test_empty_service_name():
    with pytest.raises(ValueError):
        register_service("", "https://example.com")

def test_name_containing_only_spaces():
    with pytest.raises(ValueError):
        register_service(" ", "https://example.com")

def test_empty_service_url():
    with pytest.raises(ValueError):
        register_service("Payment", "")

def test_invalid_service_url():
    with pytest.raises(ValueError):
        register_service("Payment", "ftp://example.com")