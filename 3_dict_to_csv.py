"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами
name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

list_of_dict = [{'name': 'Tom', 'age': 28, 'job': 'Engineer'},
                {'name': 'Ann', 'age': 30, 'job': 'SW developer'},
                {'name': 'Max', 'age': 21, 'job': 'Student'},
                ]


def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as file_to_create:
        keys = ['name', 'age', 'job']
        writer = csv.DictWriter(file_to_create, keys, delimiter=';')
        writer.writeheader()
        writer.writerows(list_of_dict)
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass


if __name__ == "__main__":
    main()
