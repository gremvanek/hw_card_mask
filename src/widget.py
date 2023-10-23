from src.masks import mask_card


def date_optimizer(date: str) -> str:
    """
    Для выборки нужных символов из строки с датой
    :param date: str :return: str
    """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


def card_full_printer(card_name_list: list[str], card_name: str, card_mask: str) -> str:
    for _ in card_name_list:
        if card_name not in card_name_list:
            print("Тип карты неизвестен")
            quit()
        else:
            pass

    return mask_card(card_mask, card_name)
