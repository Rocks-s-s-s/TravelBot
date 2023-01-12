def ReadFile(filename):
    file = open('tours.csv', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    return data

def Distinct_type_rest(filename):
    #чиатем данные из файла
    filedata = ReadFile(filename)
    for line in filedata:
        pass
