"""
    TODO: 1. Работа с крупным файлом.
          2.
          3. Исследовать каждую функцию и исправить проблемы, которые возникли после разделения на два файла.

"""
from user_action import *

while True:
    print("Выберите действие")
    print("1 - Найти тур")
    print("2 - Добавить новый тур")
    print("3 - Показать все туры")
    print("0 - Выход")

    choice = int(input())

    if choice == 1:
        print_tours(find_a_tour())
    if choice == 2:
        add_new_tour(read_file(filename='tours.csv'))
    if choice == 3:
        print_tours(read_all_file())
    if choice == 0:
        break
