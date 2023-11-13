import os
from datetime import datetime

from src.decorators import log


def test_log_to_file() -> None:
    """Тест логирования в файл."""
    filename = "my.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(file_name=filename)
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(1, 2)

    with open(filename, "r") as f:  # открыли файл и прочитали что в него записалось
        log_info = f.read().rstrip()

    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    expected_log_info = f"{now} Function called my_function Result: ok"
    assert log_info == expected_log_info  # сверили результат с ожидаемым


def test_log_error_to_file() -> None:
    """Тест логирования в файл ошибки."""
    filename = "my.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(file_name=filename)
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(1, 0)

    with open(filename, "r") as f:  # открыли файл и прочитали что в него записалось
        log_info = f.read().rstrip()

    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    expected_log_info = now + " Function called my_function Result: Error: division by zero. Inputs: ((1, 0), {})"
    assert log_info == expected_log_info  # сверили результат с ожидаемым
