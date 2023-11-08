import pytest

from src.decorators import my_function


@pytest.fixture
def lines() -> str:
    """
    Запись данных в строку
    :return: list[str]
    """
    with open("./my_log.txt", "r+", encoding="utf-8") as file:
        null_list = file.read()
        return null_list


def test_file_open(lines: str) -> None:
    """
    Проверка содержимого файла
    :param lines: str
    :return: None
    """
    new_line = lines.split("\n")
    assert new_line[0][20:] == "Function called my_function with args: (2, 2) . Result: 1.0"
    assert new_line[1][20:] == "Function called my_function with args: (4, 2) . Result: 2.0"
    assert new_line[2][20:] == "Function called my_function with args: (6, 2) . Result: 3.0"


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 2, "Function called my_function with args: (2, 2) . Result: 1.0\n"),
        (4, 2, "Function called my_function with args: (4, 2) . Result: 2.0\n"),
        (6, 2, "Function called my_function with args: (6, 2) . Result: 3.0\n"),
    ],
)
def test_log(x: int, y: int, expected: str) -> None:
    """
    Проверка работы декоратора log при отсутствии файла
    :param x: int
    :param y: int
    :param expected: str
    :return: None
    """
    new_func = my_function(x, y)
    for _ in expected:
        assert new_func[20:] == expected
