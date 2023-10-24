def mask_card(card: str) -> str:
    """Возвращаем результат в необходимом виде XXXX XX** **** XXXX
    :param card: in main.py
    :param card
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    card_list = card.split(" ")
    return (
        card_list[0] + " " + card_list[1] + " " + card_list[2][0:4] + " " + card_list[2][4:6] + "** **** " + card[-4:]
    )


def mask_check(check_mask: str) -> str:
    """Возвращаем результат в необходимом виде **XXXX
    :param check_mask
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    card_check = check_mask.split(" ")
    return "**" + card_check[1][-4:]
