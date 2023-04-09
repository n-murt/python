from random import randint

# Вводим количество кустов N
n = int(input('Количество кустов на грядке N:'))
# Объявляем переменную грядка
cluster = []
# Наполняем кусты ягодами
for i in range(n):
    cluster.append(randint(1, 9))

# Создаем множество, содержащее количество ягод в 3-х соседних кустах в зависимости от выбранного куста
berrys = set()
for i in range(len(cluster) - 1):
    berrys.add(cluster[i - 1] + cluster[i] + cluster[i + 1])

# Выводим содержимое грядки
print("Ягоды на кустах грядки ", cluster[:])
print(berrys)
# Выводим максимальное количество ягод которые можно собрать с 3-х соседних кустов
print("Максимальное количество ягод ", max(berrys))
