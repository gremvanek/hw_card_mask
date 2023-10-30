import pytest

from src.processing import sum_divisible_by_3_or_5


@pytest.fixture
def lst_test():
    return [[0], [1, 3, 4, 6, 7], [1, 2, 3, 4, 5]]


@pytest.mark.parametrize("lst_test, expected", [([0], 0), ([1, 3, 4, 6, 7], 0), ([1, 2, 3, 4, 5], 8)])
def sum_divisible_by_3_or_5(lst_test: list, expected):
    assert sum_divisible_by_3_or_5(lst_test) == expected
