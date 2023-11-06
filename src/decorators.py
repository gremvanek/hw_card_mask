from datetime import datetime
from typing import Any


def log(func: Any) -> Any:
    """
    Декоратор для записи результатов выполнения функций с временем выполнения
    :param func: Any
    :return: Any
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Функция для печати результата в консоль или файл
        :param filename: Any
        :param args: Any
        :param kwargs: Any
        :return: Any
        """
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        result = func(*args, **kwargs)
        filename = 'my_log.txt'
        if not filename:
            print(
                f"{str_current_datetime} Function called {func.__name__} with args: {args}"
                f"and kwargs: {kwargs}. Result: {result}"
            )
        else:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(
                    f"{str_current_datetime} Function called {func.__name__} with args: {args}"
                    f"and kwargs: {kwargs}. Result: {result}\n"
                )

    return wrapper


@log
def my_function(x: int, y: int) -> int:
    """
    Функция из дз
    :param x: int
    :param y: int
    :return: int
    """
    return x + y
