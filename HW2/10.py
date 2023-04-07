from random import randint

# Вводим число монет
n = int(input('Введите число монет:'))
# Задаем начальное число орлов
heads = 0
# Задаем начальное число решек
tails = 0

# Заполняем случайными числами
for i in range(n):
    k = randint(0, 1)
    if k == 0:
        heads += 1
    else:
        tails += 1
print('Количество орлов', heads)
print('Количество решек', tails)
# Проверяем если орлов больше или равно решек, то минимальное количество соответствует решкам
if heads >= tails:
    print('Результат:', tails)
else:
    print('Результат:', heads)
