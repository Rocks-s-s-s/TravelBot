"""
    TODO: 1. Переделать функцию print_tours()
          2. (Попробовать) Добавить файл с типами отдыха. В главной таблице будет указываться номер типа отдыха.
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
        data = []
        data = read_all_file()
        print_tours(data)
    if choice == 0:
        break
