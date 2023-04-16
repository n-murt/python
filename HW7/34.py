# Вводим стих
lyrics = input('Введите стих:')


# Объявляем функцию распознавания рифм
def rhyme_recognition(input_text):
    # Объявляем массив для подсчета рифм
    list_counts = []
    # разделяем строки
    phrases = input_text.split()
    for phrase in phrases:
        counts = 0
        # Перебираем фразы по буквам
        for letter in phrase:
            # Проверяем гласная ли буква
            if letter in 'ауоыиэяюёе':
                counts += 1
        # Записываем количество гласных во фразе
        list_counts.append(counts)
        # Выводим фразы
        print(phrase, "Количество слогов - ", counts)
    return len(list_counts) == list_counts.count(list_counts[0])


# Проверяем на рифму
if rhyme_recognition(lyrics):
    print('Результат: Парам пам-пам')
else:
    print('Результат: Пам парам')
