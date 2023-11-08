from datetime import datetime
from functools import wraps
from typing import Any, Callable, Tuple


def log(file_name: Any = None) -> Callable:
    def wrapper(func: Any) -> Callable[[tuple[Any, ...]], str]:
        @wraps(func)
        def inner(*args: Any) -> str:
            result = func(*args)
            current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            str_current_datetime = str(current_datetime)
            if file_name is not None:
                with open("./my_log.txt", "a+", encoding="utf-8") as f:
                    f.write(
                        f"{str_current_datetime} Function called {func.__name__} with args: {args} "
                        f". Result: {result}\n"
                    )
                    return (
                        f"{str_current_datetime} Function called {func.__name__} with args: {args} "
                        f". Result: {result}\n"
                    )
            else:
                return (
                    f"{str_current_datetime} Function called {func.__name__} with args: {args} "
                    f". Result: {result}\n"
                )

        return inner

    return wrapper


@log(file_name="my_log.txt")
def my_function(x: int, y: int) -> float:
    """
    Функция из дз
    :param x: int
    :param y: int
    :return: int
    """
    return x / y
