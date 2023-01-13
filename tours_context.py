def read_file(filename):
    file = open('tours.csv', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    return data

def get_types_rest(filename):
    # читаем данные из файла
    filedata = read_file(filename)
    for line in filedata:
        pass
