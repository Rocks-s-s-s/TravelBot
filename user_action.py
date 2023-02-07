from tours_context import *


def print_tours(tours):
    pass
    # TODO: Вывод таблицы туров


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
    types = get_types_rest(filename)
    countries = []
    num = 0
    correct_input = False
    save_type = 0
    print('Выберите тип отдыха (для выбора типа отдыха введите его номер):')
    for line in types:
        num += 1
        # TODO: Использовать f'' форматирование
        print('%d - %s' % (num, line))
    print('> ', end='')
    while not correct_input:
        choice = int(input())
        if choice <= len(types):
            # TODO: Использовать f'' форматирование
            print("Выбран тип отдыха - ", types[choice - 1])
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
        # TODO: Использовать f'' форматирование
        print('%d - %s' % (num, line))
    print('> ', end='')
    while not correct_input:
        choice = int(input())
        if choice <= len(countries):
            # TODO: Использовать f'' форматирование
            print("Выбранная страна - ", countries[choice - 1])
            correct_input = True
        else:
            print("Некорректный ввод")

    tours = get_tours(filename, types[save_type - 1], countries[choice - 1])
    return tours