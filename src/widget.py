def date_optimizer(date: str) -> str:
    """
    Для выборки нужных символов из строки с датой
    :param date: str :return: str
    """
    return date[8:10] + "." + date[5:7] + "." + date[0:4]
