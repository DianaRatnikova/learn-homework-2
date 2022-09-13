"""
Домашнее задание №2

Работа с файлами

1. Скачайте файл по ссылке
https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную,
подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    with open('referat.txt', 'r', encoding='utf-8') as file_referat:
        str_from_file = file_referat.read()
    print(f"количество слов: {len(str_from_file.split())}")
    str_replaced = str_from_file.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as file_referat2:
        file_referat2.write(str_replaced)
        print("Новый файл создан")

    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass


if __name__ == "__main__":
    main()
