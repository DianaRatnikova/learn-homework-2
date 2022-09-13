"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    dt_now = datetime.now()
    print(f"Сегодня: {dt_now}")
    print(f"Вчера: {dt_now -  timedelta(days=30)}")
    print(f"30 дней назад: {dt_now - timedelta(days=30)}")


def str_2_datetime(date_string):
    str_date = "01/01/20 12:10:03.234567"
    date_from_str = datetime.strptime(str_date, "%d/%m/%y %H:%M:%S.%f")
    return date_from_str


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
