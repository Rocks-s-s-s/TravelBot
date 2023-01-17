def read_file(filename):
    file = open(filename, encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    return data

def get_types_rest(filename):
    # читаем данные из файла
    filedata = read_file(filename)
    uniquetype = []
    first = 0
    for line in filedata:
        x = 0
        if first == 0:
            first = 1
            continue
        for i in range(len(uniquetype)):
            if uniquetype[i] != line[3]:
                x = x + 1
        if x == len(uniquetype):
            uniquetype.append(line[3])
    return uniquetype

filename = "tours.csv"
uniquetype = get_types_rest(filename)
print(uniquetype)