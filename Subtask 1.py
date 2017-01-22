from functools import wraps
from pprint import pprint as pp


def a_decorator(func):
    @wraps(func)
    def wrapper(arg1):
        def func(arg2):
            return arg1 + arg2
        return func
    return wrapper


@a_decorator
def add_factory_three(arg2):
    return arg2

if __name__ == "__main__":
    add7 = add_factory_three(7)
    pp(add7(10))
