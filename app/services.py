from urllib.parse import urlparse


def validate_service(name, url):
    if not name or not name.strip():
        raise ValueError("Invalid service name")

    if not url or not url.strip():
        raise ValueError("Invalid service URL")

    result = urlparse(url)

    if result.scheme not in ("http", "https") or not result.hostname:
        raise ValueError("Invalid service URL")


def register_service(name, url, services):
    validate_service(name, url)

    if get_service(name, services):
        raise ValueError("Service already exists")

    service = {
        "name": name,
        "url": url,
        "status": "unknown"
    }

    services.append(service)
    return service


def get_service(name, services):
    for service in services:
        if service["name"] == name:
            return service

    return None


def get_all_services(services):
    return services