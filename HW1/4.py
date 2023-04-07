# Вводим трехзначное число
number = int(input('Введите трехзначное число:'))
# Вычисляем количество сотен
number_100 = number // 100
# Вычисляем количество десятков
number_10 = (number - number_100 * 100) // 10
# Вычисляем количество единиц
number_1 = number - number_100 * 100 - number_10 * 10
# Складываем
amount = number_100 + number_10 + number_1
# Выводим результат
print('Результат:', amount)
