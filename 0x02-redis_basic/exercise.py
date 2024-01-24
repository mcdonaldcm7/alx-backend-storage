#!/usr/bin/env python3
"""
This module contains the class definition for Cache
"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable[[Any, Union[str, bytes, int, float]], str]
                ) -> Callable[[Any, Union[str, bytes, int, float]], str]:
    """
    Wrapper for method
    """
    @wraps(method)
    def wrapper(self: "Cache", data: Union[str, bytes, int, float]) -> str:
        """
        Keep count number of times method has been called
        """
        self._redis.incr(method.__qualname__)
        return method(self, data)
    return wrapper


def call_history(method: Callable[[Any, Union[str, bytes, int, float]], str]
                 ) -> Callable[[Any, Union[str, bytes, int, float]], str]:
    """
    Creates and/or append the input and output of method to the list ":input"
    and ":output" list keys respectively where the name of both list are
    appended by the decorated function's qualified name
    """
    @wraps(method)
    def wrapper(self: "Cache", *args, **kwargs) -> str:
        """
        """
        key_input = "{}:inputs".format(method.__qualname__)
        key_output = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(key_input, str(args))

        # Execute and store the result of the decorated function
        output = method(self, *args, **kwargs)

        self._redis.rpush(key_output, output)
        return output
    return wrapper


def replay(method):
    """
    """
    @wraps(method)
    def wrapper(self):
        """
        """
        key_input = "{}:inputs".format(method.__qualname__)
        key_output = "{}:outputs".format(method.__qualname__)
        inputs = self.get(key_input)
        outputs = self.get(key_output)
        print("Inputs are {}".format(inputs))
        print("Outputs are {}".format(outputs))
    return wrapper


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate a random key using uuid, store the input data in Redis using
        the random key and returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """
        Retrieves the data from the redis server associated with the key passed
        and uses the callable function (if passed) fn to convert the data back
        to the desired format
        """
        if self._redis.exists(key):
            if fn is None:
                return self._redis.get(key)
            return fn(self._redis.get(key))
        return None

    def get_str(self, key: str, fn=str) -> str:
        """
        Modification of Cache.get to automatically parametrize it with the
        string conversion function str
        """
        return self.get(key, fn)

    def get_int(self, key: str, fn=int) -> int:
        """
        Modification of Cache.get to automatically parametrize it with the
        integer conversion function int
        """
        return self.get(key, fn)
