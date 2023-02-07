def read_file(filename):
    file = open(filename, encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    return data

def write_file(data,filename):
    file = open(filename, encoding='utf-8', mode="w")
    for line in data:
        fileline = ''
        #for i in range(8):
            #fileline = fileline + str(line[i]) + ','
        file.write(','.join(line) + '\n')


def get_types_rest(filename):
    # Читаем данные из файла
    # С помощью среза избавляемся от заголовков
    filedata = read_file(filename)[1:]
    # Используем set() множество для того, чтобы выделить уникальные строки
    types = set()
    for line in filedata:
        types.add(line[3])
    return types


def get_country_by_type(filename, type):
    filedata = read_file(filename)[1:]
    country = set()
    for line in filedata:
        if type == line[3]:
            country.add(line[0])
    return country


def get_tours(filename, type, country):
    filedata = read_file(filename)[1:]
    tours = []
    for line in filedata:
        if country == line[0] and type == line[3]:
            tours.append(line)
    return tours
