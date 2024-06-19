#!/usr/bin/env python3
'''A module for using the Redis NoSQL data storage.
'''
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    '''Represents a cache storage using Redis.
    
    This class allows for storing and retrieving data in a Redis database
    using randomly generated keys.
    '''
    def __init__(self) -> None:
        '''Initializes a Cache instance.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores a value in a Redis data storage and returns the key.
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
