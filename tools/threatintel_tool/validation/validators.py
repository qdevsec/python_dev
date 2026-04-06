# IOC Validator

import ipaddress
from urllib.parse import urlparse
import validators

def is_valid_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

def is_valid_domain(value: str) -> bool:
    return validators.domain(value)

def is_valid_url(value: str) -> bool:
    if not validators.url(value):
        return False
    parsed = urlparse(value)
    return all([parsed.scheme, parsed.netloc])

def validate_ioc(ioc_type: str, value: str) -> bool:
    if ioc_type == "ip":
        return is_valid_ip(value)
    elif ioc_type == "domain":
        return is_valid_domain(value)
    elif ioc_type == "url":
        return is_valid_url(value)
    return False