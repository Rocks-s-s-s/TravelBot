from tours_context import *


def print_tours(data):
    title = ["Страна", "Город", "Название тура", "Тип отдыха", "Стоимость", "Дата начала", "Дата окончания"]
    type = get_types()
    print('-----------------------------------------------------------------------------------------------------------')
    print(
        f'| {title[0]:10} | {title[1]:10} | {title[2]:15} | {title[3]:15} | {title[4]:10} | {title[5]:11} | {title[6]:14} |')
    print(
        '|---------------------------------------------------------------------------------------------------------|')
    for line in data:
        print(
            f'| {line[0]:10} | {line[1]:10} | {line[2]:15} | {type[line[3]]:15} | {line[4]:10} | {line[5]:11} | {line[6]:14} |')
        print(
            '|---------------------------------------------------------------------------------------------------------|')


def read_all_file():
    data = read_file("tours_1000000.csv")
    return data


# TODO: Ожидается проблема при добавлении, т.к. мы добавляем название типа отдыха, а у нас в таблице хранятся номера.
#       Значит нужно проверять есть ли такой тип отдыха и, если есть, возвращать его код, а если нет, то добавлять его
#       в таблицу типов и также, возвращать его код.
def add_new_tour(tours):
    line = []
    headers = ["Страна", "Город", "Название тура", "Тип отдыха", "Стоимость", "Дата начала", "Дата окончания"]
    for head in headers:
        print(f'Введите {head}: ')
        line.append(input())
    tours.append(line)
    write_file(tours, filename='tours.csv')


def print_all():
    print_tours(read_file(filename='tours_1000000.csv'))


def find_a_tour():
    filename = 'tours_1000000.csv'
    types = get_types()
    countries = []
    num = 0
    correct_input = False
    save_type = 0
    print('Выберите тип отдыха (для выбора типа отдыха введите его номер):')
    for line in types:
        num += 1
        print(f'{num} - {line}')
    print('> ', end='')

    choice = input()
    if choice in types:
        print(f'Выбран тип отдыха - {types[choice]}')
        save_type = choice

    else:
        print("Некорректный ввод")
    correct_input = False
    country = get_country_by_type(filename, types[choice])
    print('Выберите страну (для выбора страны введите её номер): ')
    num = 0
    for line in country:
        num += 1
        countries.append(line)
        print(f'{num} - {line}')
    print('> ', end='')
    while not correct_input:
        choice = int(input())
        if choice <= len(countries):
            print(f"Выбранная страна - {countries[choice]}")
            correct_input = True
        else:
            print("Некорректный ввод")

    tours = get_tours(filename, types[save_type], countries[choice - 1])
    return tours
