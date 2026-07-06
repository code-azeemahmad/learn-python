'''Problem: Implement a decorator that caches the return 
values of a function, so that when it's called with the
same arguments, the cached value is returned instead of 
re-executing the function.'''

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def longRunningFunc(a, b):
    time.sleep(4)
    return a + b


print(longRunningFunc(2, 6))    # takes 4 seconds, and add in cache_value
print(longRunningFunc(2, 6))    # cache from cache_value, no delay
print(longRunningFunc(2, 3))


'''*args collects all extra positional arguments into a tuple, 
and **kwargs collects all keyword arguments into a dictionary.'''