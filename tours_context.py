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
