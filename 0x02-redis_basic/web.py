#!/usr/bin/env python3
"""
Caching request module
"""
from functools import wraps
from typing import Callable
import requests
import redis


def track_get_page(fn: Callable) -> Callable:
    """Decorator for get_page"""

    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper that:
        - check whether a url's data is cached
        - tracks how many times get_page is called
        """
        client = redis.Redis()
        client.incr(f"count:{url}")
        cached_page = client.get(f"{url}")
        if cached_page:
            return cached_page.decode("utf-8")
        response = fn(url)
        client.set(f"{url}", response, 10)
        return response

    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """
    Args:

        url: url to get
    Returns:

            the HTML content of the URL
    """
    response = requests.get(url)
    return response.text
