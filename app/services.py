from urllib.parse import urlparse

def validate_service(name, url):
    result = urlparse(url)
    if not name or not name.strip():
        raise ValueError("Invalid service name")
    
    if not url or not url.strip():
        raise ValueError("Invalid service")
    
    if result.scheme not in ("http", "https") or not result.hostname:
        raise ValueError("Invalid service URL")



def register_service(name, url):
    validate_service(name,url)
    
    services= {
        "name": name,
        "url": url,
        "status": "unknown"
    }
    return services