from src.masks import mask_card


def date_optimizer(date: str) -> str:
    """
    Для выборки нужных символов из строки с датой
    :param date: str :return: str
    """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


def card_full_printer(card_list: list[str]) -> str:
    return mask_card(card_list)
