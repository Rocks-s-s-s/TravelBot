"""
    TODO: 1. Создать главный цикл работы программы с возможностью выбирать различные действия:
             1 - Найти тур
             2 - Добавить новый тур (пока не реализовывать)
             3 - Показать все туры
             0 - Выход
             Каждый пункт в своей функции.
          2. Сделать форматированый вывод найденого тура.
          3. Сделать режим работы по добалению тура в файл (перезапись информации в файле)
"""
# Такое подключение лучше, т.к. не нужно писать название модуля, а просто название функции
from tours_context import *
from UserAction import *

toggle = 0
while toggle != 1:
    print("Выберите действие")
    print("1 - Найти тур")
    print("2 - Добавить новый тур")
    print("3 - Показать все туры")
    print("0 - Выход")

    choice1 = int(input())

    if choice1 == 1:
        tours = []
        tours = find_a_tour()
        format_print_tour(tours)
    if choice1 == 2:
        tours = []
        tours = read_file(filename='tours.csv')
        add_new_tour(tours)
    if choice1 == 3:
        find_all()
    print('Вы хотите продолжить использование программы?')
    choice2 = input()
    if choice2 == "No" or choice2 == "no" or choice2 == "Нет" or choice2 == "нет" or  choice2 == "-" :
        toggle == 1
