"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def print_days():
    today = datetime.now()

    delta = timedelta(days=1)
    yesterday = today - delta

    delta = timedelta(days=30)
    last_month = today - delta

    print(yesterday)
    print(today)
    print(last_month)

def str_2_datetime(date_string):
    dt_date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dt_date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
