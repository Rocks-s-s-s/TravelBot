def read_file(filename):
    file = open(filename, encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    return data


def get_types_rest(filename):
    # Читаем данные из файла
    # С помощью среза избавляемся от заголовков
    filedata = read_file(filename)[1:]
    # Используем set() множество для того, чтобы выделить уникальные строки
    types = set()
    for line in filedata:
        types.add(line[3])
    return types

def get_country_by_type(filename,type):
    #читаем файлы из файла
    filedata = read_file(filename)[1:]
    contry = set()
    for line in filedata:
        if type == line[3]:
            contry.add(line[0])
    return contry

def get_tours(filename,type, country):
    filedata = read_file(filename)[1:]
    tyrse = []
    for line in filedata:
        if country == line[0] and type == line[3]:
            tyrse.append(line)
    return tyrse


#type= "Пляжный"
#country =  "Бали"
#tyrse = get_tours(filename="tours.csv",type = type, country = country)
#print(tyrse)