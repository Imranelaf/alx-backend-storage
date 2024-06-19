#!/usr/bin/env python3
'''A module with tools for caching and tracking web page requests.
'''
import redis
import requests
from functools import wraps
from typing import Callable


cache = redis.Redis()
'''The module-level Redis instance for caching and tracking.
'''


def cache_request(method: Callable) -> Callable:
    '''Decorator to cache the output of a function that fetches web page data.
    '''
    @wraps(method)
    def wrapper(url: str) -> str:
        '''Caches the result of the method and tracks the number of requests.
        '''
        # Increment the request count for the URL
        cache.incr(f'count:{url}')
        # Check if the result is already cached
        cached_result = cache.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        # Fetch the result and cache it
        result = method(url)
        cache.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@cache_request
def get_page(url: str) -> str:
    '''Fetches and returns the content of a URL,
    with caching and request tracking.
    Args:
        url (str): The URL to fetch.
    Returns:
        str: The content of the URL.
    '''
    return requests.get(url).text
