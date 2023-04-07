from random import randint

# Объявляем счетчик
count = 0
# Вводим размер списка N
n = int(input('Размер списка N:'))
# Создаем список
new_list = []
# Наполняем список
for i in range(n):
    new_list.append(randint(1, 9))
# Выводим список
print(new_list[:])

# Вводим число для поиска X
x = int(input('введите число X, количества вхождений которого надо подсчитать:'))

for i in range(len(new_list)):

    if new_list[i] == x:
        count += 1

print('Количество Количество вхождений:', count)
