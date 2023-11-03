import pytest

from src.masks import mask_card, mask_check


@pytest.fixture
def card_mask_test() -> list[str]:
    """
    Список строк для проверки функции card_mask
    :return:list[str]
    """
    return ["15968705199", "715830726758", "7000792289606361"]


@pytest.mark.parametrize(
    "card_mask_test, expected",
    [
        ("15968705199", "Введенные данные неверные"),
        ("715830726758", "Введенные данные неверные"),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_mask_card(card_mask_test: str, expected: str) -> None:
    assert mask_card(card_mask_test) == expected


@pytest.fixture
def check_out_mask_test() -> list[str]:
    """
    Возвращает список строк
    :return: list[str]
    """
    return ["64686473", "353830334789556", "73654108430135874305"]


@pytest.mark.parametrize(
    "check_out_mask_test, expected",
    [
        ("64686473", "Введенные данные неверные"),
        ("353830334789556", "Введенные данные неверные"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_check_mask(check_out_mask_test: str, expected: str) -> None:
    assert mask_check(check_out_mask_test) == expected
