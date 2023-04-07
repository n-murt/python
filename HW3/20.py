# Объявляем список баллов
list_points = [1, 2, 3, 4, 5, 8, 10]
# Объявляем список английских букв
list_en_chars = [["A", "E", "I", "O", "U", "L", "N", 'S', "T", "R"], ["D", "G"], ["B", "C", "M", "P"],
                 ["F", "H", "V", "W", "Y"], ["K"], ["J", "X"], ["Q", "Z"]]
# Объявляем список русских букв
list_ru_chars = [["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"], ["Д", "К", "Л", "М", "П", "У"],
                 ["Б", "Г", "Ё", "Ь", "Я"], ["Й", "Ы"], ["Ж", "З", "Х", "Ц", "Ч"], ["Ш", "Э", "Ю"], ["Ф", "Щ", "Ъ"]]

dict_en = {}
dict_ru = {}
amount = 0

for i in range(len(list_points)):
    # Генерируем словарь для оценки английский
    for j in range(len(list_en_chars[i])):
        dict_en[list_en_chars[i][j].lower()] = list_points[i]
    # Генерируем словарь для оценки русский
    for j in range(len(list_ru_chars[i])):
        dict_ru[list_ru_chars[i][j].lower()] = list_points[i]

# Если надо вывести словари для проверки
# for key, value in dict_en.items():
#    print("{0}: {1}".format(key, value))

# Вводим слово
word = str(input('Введите слово:'))
# Проверяем по первой букве английское или русское слово
if word[0].lower() in dict_en:
    for i in range(len(word)):
        amount += int(dict_en.get(word[i].lower()))

elif word[0].lower() in dict_ru:
    for i in range(len(word)):
        amount += int(dict_ru.get(word[i].lower()))
else:
    print('Неверное слово')
    exit()

print('Количество баллов:', amount)
