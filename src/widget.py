from src.masks import mask_card, mask_check


def date_optimizer(date: str) -> str:
    """
    Для выборки нужных символов из строки с датой
    :param date: str :return: str
    """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


def card_full_printer(card: str, check_mask: str):
    print(mask_card(card))
    print('')
    print(f"Счет {mask_check(check_mask)}")
