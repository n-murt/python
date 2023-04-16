# Вводим количество строк
rows = int(input("Введите количество строк: "))
# Вводим количество столбцов
columns = int(input("Введите количество столбцов: "))


# Объявляем функцию распознавания рифм
def print_operation_table(operation, rows_num=6, columns_num=6):
    # Наполняем массив начинаем не с 0, что бы не умножать на 0
    for i in range(1, rows_num + 1):
        result = []
        # Перебираем массив
        for j in range(1, columns_num + 1):
            result.append(str(operation(i, j)))
        # выводим строку
        print(''.join(f'{e:<3}' for e in result))


# Вызываем функцию
print_operation_table(lambda x, y: x * y, rows, columns)
