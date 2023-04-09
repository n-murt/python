from random import randint

# Вводим размеры наборов данных
n = int(input('Введите размер набора1 N:'))
m = int(input('Введите размер набора2 M:'))
# Объявляем наборы данных
list1 = []
list2 = []
# Наполняем наборы данных
for i in range(n):
    list1.append(randint(1, 9))
for i in range(m):
    list2.append(randint(1, 9))
print("Набор данных1:", list1[:])
print("Набор данных2:", list2[:])
# Переводим списки в множества
set1 = set(list1)
set2 = set(list2)
# Объединяем множества
merge = set1 & set2
# Выводим без повторений в порядке возрастания числа из множества
print("Результат:", sorted(merge))