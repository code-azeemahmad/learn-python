'''Problem: Write a decorator that measures 
the time a function takes to execute.'''

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        duration = end - start
        print(f"{func.__name__} ran in: {duration:.6f} seconds")
        return result
    return wrapper


@timer  # python internally does: exampleFunc = timer(exampleFunc), now exampleFunc actually calls wrapper
def exampleFunc(n):
    time.sleep(n)

exampleFunc(2)


# learn functools.wraps to preserve the original function's metadata.