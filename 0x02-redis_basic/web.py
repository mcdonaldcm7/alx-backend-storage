#!/usr/bin/python3
"""
Task

5. Implementing an expiring web cache and tracker

In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of the function is very
simple. It uses the requests module to obtain the HTML content of a particular
URL and returns it.

Start in a new file named web.py and do not reuse the code written in
exercise.py.

Inside get_page track how many times a particular URL was accessed in the key
"count:{url}" and cache the result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response and
test your caching.

Bonus: implement this use case with decorators.
"""
import requests
import redis
from functools import wraps
from datetime import timedelta


Cache = __import__('exercise').Cache


c = Cache()


def url_calls(method):
    """
    Decorator function to count calls to a 'url'
    """
    @wraps(method)
    def wrapper(url):
        """
        URL Counter
        """
        key = "count:{}".format(url)
        c.incr(key)
        return method(url)
    return wrapper


@url_calls
def get_page(url: str) -> str:
    """
    Obtains the HTML content of a particular URL and returns it
    """
    key = "page:{}".format(url)

    if c.exists(key):
        return c.get(key).decode('utf-8')

    response = requests.get(url)
    html_content = response.text
    c.store(page, html_content)
    c._redis.expire(key, timedelta(seconds=10))
    return html_content
