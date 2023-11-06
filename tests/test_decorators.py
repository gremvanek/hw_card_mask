import pathlib

import pytest

from src.decorators import log, my_function

filename = pathlib.Path('my_log.txt')
with open(filename, 'r', encoding='utf-8') as f:
    f_line = f.readline()


@pytest.fixture
def test_log() -> str:
    """
    Функция для проверки log
    :return: str
    """
    assert log(my_function) == f_line
