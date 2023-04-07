from random import randint

# Вводим размер списка N
n = int(input('Размер списка N:'))
# Создаем список
new_list = []
# Наполняем список
for i in range(n):
    new_list.append(randint(1, 99))
# Выводим список
print(new_list[:])

# Вводим число для поиска X
x = int(input('введите число X, ближайшее к которому надо найти в массиве:'))
# Объявляем счетчик равный первому элементу массива
like = new_list[0]
for i in range(len(new_list)):
    if abs(new_list[i] - x) < abs(like - x):
        like = new_list[i]
print('Самое близкое число в массиве:', like)
