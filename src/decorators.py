from datetime import datetime
from functools import wraps


def log(file_name=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args):
            result = func(*args)
            current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            str_current_datetime = str(current_datetime)
            if file_name is not None:
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(f"{str_current_datetime} Function called {func.__name__} with args: {args} "
                            f". Result: {result}\n")
            else:
                print(f"{str_current_datetime} Function called {func.__name__} with args: {args} "
                      f". Result: {result}\n")

        return inner

    return wrapper


@log()
def my_function(x: int, y: int) -> int:
    """
    Функция из дз
    :param x: int
    :param y: int
    :return: int
    """
    return x + y
