from random import randint

# Вводим размер массива, min и max
n = int(input('Введите размер массива:'))
min = int(input('Введите min:'))
max = int(input('Введите max:'))
# Объявляем массивив первоначальный и конечный
list_data = []
result = []
# Наполняем массив
for i in range(n):
    list_data.append(randint(1, 9))
# Выводим массив
print('Массив:', list_data[:])
# Перебираем массив
for (index, item) in enumerate(list_data):
    if item >= min and item <= max:
        result.append(index)

# Выводим результат
print('Результат:', result[:])
