"""
    TODO: 1. (Продолжить...) Добавить файл с типами отдыха (Номер типа, Название типа).
             В главной таблице будет указываться номер типа отдыха.
             Это, по идее, очень сильно повлияет на весь код.
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
