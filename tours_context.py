

def ReadFile(filename):
    file = open(r'tour.csv', encoding='utf-8')

    filePhrases = []

    for line in file:
        filePhrases.append(line.strip().split(','))
