from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(file_name: str | None = None) -> Callable:
    """
    Декоратор для проверки функций
    :param file_name: str | None
    :return: Callable
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            status = "ok"
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                result = None
                status = f"Error: {e}. Inputs: {args, kwargs}"
            current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            log_info = f"{current_datetime} Function called {func.__name__} Result: {status}"
            if file_name:
                with open(file_name, "a+", encoding="utf-8") as f:
                    f.write(log_info + "\n")
            else:
                print(log_info)
            return result

        return wrapper

    return decorator


@log("my.txt")
def my_function(x: int, y: int) -> float:
    """
    Функция для проверки декоратора
    :param x: int
    :param y: int
    :return: int
    """
    return x + y


print(my_function(1, 2))
