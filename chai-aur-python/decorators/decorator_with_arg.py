from functools import wraps

def repeat(times):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):  # Repeat this block of code times times, but I don't care about the loop variable
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)  # internally, hello = repeat(3)(hello)
def hello():    
    print("Hello")


hello()