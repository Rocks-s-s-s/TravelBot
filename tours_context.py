def read_file(filename):
    file = open(filename, encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    file.close()
    return data


def write_file(data, filename):
    file = open(filename, encoding='utf-8', mode="w")
    for line in data:
        file.write(f'{",".join(line)}\n')
    file.close()

def get_typs():
    type = {}
    filetype = read_file("type.csv")
    for line in filetype:
        type[line[0]] = line[1]
    return type


def get_types_rest(filename):
    types = {}
    filedata = read_file(filename)
    for line in filedata:
        types.add(line[3])
    return types


def get_country_by_type(filename, type):
    filedata = read_file(filename)
    country = set()
    for line in filedata:
        if type == line[3]:
            country.add(line[0])
    return country


def get_tours(filename, type, country):
    filedata = read_file(filename)
    tours = []
    for line in filedata:
        if country == line[0] and type == line[3]:
            tours.append(line)
    return tours
