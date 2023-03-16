import random
import string
import time


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


def get_types():
    type = {}
    filetype = read_file("type.csv")
    for line in filetype:
        type[line[0]] = line[1]
    return type


def get_country_by_type(filename, type):
    filedata = read_file(filename)
    country = set()
    types = get_types()
    for line in filedata:
        if type == types[line[3]]:
            country.add(line[0])
    return country


def get_tours(filename, type, country):
    filedata = read_file(filename)
    tours = []
    for line in filedata:
        if country == line[0] and type == line[3]:
            tours.append(line)
    return tours


def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d.%m.%Y', prop)


# ["Страна", "Город", "Название тура", "Тип отдыха", "Стоимость", "Дата начала", "Дата окончания"]
def generate_large_tours_file(size):
    f = open(f'tours_{size}.csv', 'a')
    for i in range(size):
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(2, 15)))
        date = random_date("3.3.2023", "3.3.2024", random.random())
        f.write(f'Страна{random.randint(1, 55)},Город{random.randint(1, 6000)},{name},{random.randint(1, 4)},'
                f'{random.randint(10000, 4000000)},{date},{random_date(date, "3.3.2024", random.random())}\n')
    f.close()


#generate_large_tours_file(1000000)
