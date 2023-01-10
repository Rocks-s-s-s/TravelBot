def ReadFile(filename):
    file = open('tours.csv', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip().split(','))
    return data
