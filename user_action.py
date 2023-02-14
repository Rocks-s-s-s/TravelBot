from tours_context import *


# TODO: Должна принемать туры для вывода в виде массива туров (нре из файла)
def print_tours(data):
    print('-----------------------------------------------------------------------------------------------------------')
    for line in data:
        print(f'| {line[0]:10} | {line[1]:10} | {line[2]:15} | {line[3]:15} | {line[4]:10} | {line[5]:11} | {line[6]:14} |')
        print('|---------------------------------------------------------------------------------------------------------|')

def read_all_file():
    data = read_file("tours.csv")
    return data


def add_new_tour(tours):
    line = []
    headers = read_file('tours.csv')[0]
    for head in headers:
        print(f'Введите: {head}')
        line.append(input())
    tours.append(line)
    write_file(tours, filename='tours.csv')


def print_all():
    # TODO: Это не форматированный вывод. Для вывода всех туров, нужно взять туры и вывести их функцией print_tours()
    data = read_file(filename='tours.csv')
    for line in data:
        print(line)


def find_a_tour():
    filename = 'tours.csv'
    types = list(get_types_rest(filename))
    countries = []
    num = 0
    correct_input = False
    save_type = 0
    print('Выберите тип отдыха (для выбора типа отдыха введите его номер):')
    for line in types:
        num += 1
        print(f'{num} - {line}')
    print('> ', end='')
    while not correct_input:
        choice = int(input())
        if choice <= len(types):
            print(f'Выбран тип отдыха - {types[choice-1]}')
            save_type = choice
            correct_input = True
        else:
            print("Некорректный ввод")
    correct_input = False
    country = get_country_by_type(filename, types[choice - 1])
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
            print(f"Выбранная страна - {countries[choice - 1]}")
            correct_input = True
        else:
            print("Некорректный ввод")

    tours = get_tours(filename, types[save_type - 1], countries[choice - 1])
    return tours
