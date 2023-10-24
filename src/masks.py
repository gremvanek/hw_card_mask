def mask_card(card_list: list[str]) -> str:
    """Возвращаем результат в необходимом виде XXXX XX** **** XXXX
    : Номер для маскирования
    :return: Маскированный по правилу номер"""
    return (
        card_list[0]
        + " "
        + card_list[1]
        + " "
        + card_list[2][0:4]
        + " "
        + card_list[2][4:6]
        + "** **** "
        + card_list[2][-4:]
    )


def mask_check(check_mask_list: list[str]) -> str:
    """Возвращаем результат в необходимом виде **XXXX
    :type check_mask_list: str
    :param check_mask_list
    : Номер для маскирования
    :return: Маскированный по правилу номер
    """
    return "**" + check_mask_list[1][-4:]
