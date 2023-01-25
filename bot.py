"""
    TODO: 1. Необходимо написать функцию travel_type_keyboard(), которая генерирует клавиатуру
             с типами отдыха и выводит на экран для выбора пользователем.
             Клавиатура появляется после приветствия бота.
          2. Необходимо написать функцию country_keyboard(type), которая генерирует клавиатуру
             с доступными по типу странами.
          3. Сделать форматированый вывод найденого тура.
          4. Сделать режим работы по добалению тура в файл
"""
import tours_context
filename = 'tours.csv'
type = tours_context.get_types_rest(filename)
num = 0
corest_imput = 0
typs = []
save_type = 0
countries =[]
print('Выберите тип отдыха(для выбора типа отдыха введите его номер):')
for line in type:
    num +=1
    typs.append(line)
    print('%d - %s' % (num,line))
while corest_imput == 0:
    choice = int(input())
    if choice <= len(typs):
        print("Выбран тип отдыха -",typs[choice-1])
        save_type = choice
        corest_imput = 1
    else:
        print("Некоректный ввод")
corest_imput = 0
coutry = tours_context.get_country_by_type(filename, type = typs[choice-1])
print('Выберите страну(для выбора страны  введите её номер):')
num = 0
for line in coutry:
    num +=1
    countries.append(line)
    print('%d - %s' % (num, line))
while corest_imput == 0:
    choice = int(input())
    if choice <= len(countries):
        print("Выбраная страна -",countries[choice-1])
        corest_imput = 1
    else:
        print("Некоректный ввод")

tours =tours_context.get_tours(filename, type= typs[save_type -1], country = countries[choice-1])
#print("Програма нашла вам подходяший тур - %s" % (tours))


