from tours_context  import *
def format_print_tour(tours):
    x = 0
    data = []
    data =read_file(filename='tours.csv')
    elemenysData = []
    for i in data[0]:
        elemenysData[i] = data[i]
    for i in tours:
        print(elemenysData[x]+"-"+tours[i])

def find_all():
    data = []
    data = read_file(filename='tours.csv')
    for line in data:
        print(line)
def find_a_tour():
    filename = 'tours.csv'
    type = get_types_rest(filename)
    num = 0
    corest_imput = 0
    typs = []
    save_type = 0
    countries = []
    print('Выберите тип отдыха(для выбора типа отдыха введите его номер):')
    for line in type:
        num += 1
        typs.append(line)
        print('%d - %s' % (num, line))
    while corest_imput == 0:
        choice = int(input())
        if choice <= len(typs):
            print("Выбран тип отдыха -", typs[choice - 1])
            save_type = choice
            corest_imput = 1
        else:
            print("Некоректный ввод")
    corest_imput = 0
    coutry = get_country_by_type(filename, type=typs[choice - 1])
    print('Выберите страну(для выбора страны  введите её номер):')
    num = 0
    for line in coutry:
        num += 1
        countries.append(line)
        print('%d - %s' % (num, line))
    while corest_imput == 0:
        choice = int(input())
        if choice <= len(countries):
            print("Выбраная страна -", countries[choice - 1])
            corest_imput = 1
        else:
            print("Некоректный ввод")

    tours = get_tours(filename, type=typs[save_type - 1], country=countries[choice - 1])
    return tours
# print("Програма нашла вам подходяший тур - %s" % (tours))