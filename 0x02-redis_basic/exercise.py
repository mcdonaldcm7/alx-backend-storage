#!/usr/bin/env python3
"""
Task

0. Writing string to Redis

Create a 'Cache' class. In the '__init__' method, store an instance of the
Redis client as a private variable named '_redis' (using 'redis.Redis()') and
flush the instance using 'flushdb'.

Create a 'store' method that takes a 'data' argument and returns a string. The
method should generate a random key (e.g. using 'uuid'), store the input data
in Redis using the random key and return the key.

Type-annotate 'store' correctly. Remember that 'data' can be a 'str', 'bytes',
'int' or 'float'.
"""
import redis
import uuid
from typing import Union, Optional, Any


class Cache:
    """
    Redis Cache class for storing and retrieving data
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data with a key and returns the key used
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Optional[Callable[[]]]) -> Union[Any, None]:
        """
        Returns the value associated with key (if any), after converting it to
        the appropriate type using fn (if provided)
        """
        if self._redis.exists(key):
            if fn is not None:
                return fn(self._redis.get(key))
            return self._redis.get(key)
        return None

    def get_str(self, key=str, fn=str) -> str:
        """
        Parametrize 'Cache.get' with the correct conversion function(str)
        """
        return self.get(key, fn)

    def get_int(self, key=int, fn=int) -> int:
        """
        Parametrize 'Cache.get' with the correct conversion function(int)
        """
        return self.get(key, fn)
