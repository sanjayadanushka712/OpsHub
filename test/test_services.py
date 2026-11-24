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

