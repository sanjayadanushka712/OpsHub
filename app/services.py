def register_service(name, url):
    if not name or not name.strip():
        raise ValueError("Invalid service name")

    if not url or not url.strip():
        raise ValueError("Invalid service")


    services= {
        "name": name,
        "url": url,
        "status": "unknown"
    }
    return services


