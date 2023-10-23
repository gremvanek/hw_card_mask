def date_optimizer(date: str) -> str:
    return date[8: 10] + '.' + date[5: 7] + '.' + date[0: 4]
