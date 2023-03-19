from tours_context import *


def print_tours(data):
    title = ["Страна", "Город", "Название тура", "Тип отдыха", "Стоимость", "Дата начала", "Дата окончания"]
    type = get_types()
    line_output = 0
    x= 1
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
        line_output += 1
        if line_output == 16:
            print("Выводить ещё страницу с поездками? Введите да для продолжения")
            choise = input()
            if choise == "да" or choise == "lf":
                x += 1
                print(f"Страница - {x}")
                line_output = 0
            else:
                break


def read_all_file():
    data = read_file("tours_1000000.csv")
    return data


# TODO: Ожидается проблема при добавлении, т.к. мы добавляем название типа отдыха, а у нас в таблице хранятся номера.
#       Значит нужно проверять есть ли такой тип отдыха и, если есть, возвращать его код, а если нет, то добавлять его
#       в таблицу типов и также, возвращать его код.
def add_new_tour(tours):
    lines = []
    file = read_file("type.csv")
    headers = ["Страна", "Город", "Название тура", "Тип отдыха", "Стоимость", "Дата начала", "Дата окончания"]
    for head in headers:
        print(f'Введите {head}: ')
        x = input()
        t =0
        if head == "Тип отдыха":
            for line in file:
                if x == line[1]:
                    lines.append(file[0])
                    t+=1
            if t ==0:
                s =str(int(line[0]) + 1) +","+ x
                add_new_type(s)
                lines.append(int(line[0]) + 1)
                print(lines[3])
        else:
            lines.append(x)

    tours.append(lines)
    write_file(tours, filename='tours.csv')

def add_new_type(file):
    types =open('type.csv', encoding='utf-8', mode="a")
    types.write(f'\n{file}')


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
    for key, value in types.items():
        print(key, '-', value)

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
    x=1
    line_output = 0
    for line in country:
        num += 1
        countries.append(line)
        print(f'{num} - {line}')
        line_output +=1
        if line_output == 16:
            print("Выводить ещё страницу с поездками? Введите да для продолжения")
            choise = input()
            if choise == "да" or choise == "lf":
                x += 1
                print(f"Страница - {x}")
                line_output = 0
            else:
                break
    print('> ', end='')
    while not correct_input:
        choice = int(input())
        if choice <= len(countries):
            print(f"Выбранная страна - {countries[choice-1]}")
            correct_input = True
        else:
            print("Некорректный ввод")

    tours = get_tours(filename, save_type, countries[choice - 1])
    return tours
