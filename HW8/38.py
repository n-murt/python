# Функция Открыть файл
def open_file(mode="r"):
    try:
        file_o = open('phonebook.txt', mode, encoding='utf-8')
    except IOError:
        file_o = open('phonebook.txt', 'w', encoding='utf-8')
        file_o = open('phonebook.txt', mode, encoding='utf-8')
        print('Файла нет, создаем пустой')
    return file_o


# Функция Сохранить файл
def save_file(data):
    with open_file('w') as fp:
        fp.writelines(data)


# Функция Чтение файла
def read_file():
    f = open_file("r")
    result = f.readlines()
    f.close()
    return result


# Функция Посмотреть все контакты
def show_all_contacts():
    i = 1
    contacts = read_file()
    if len(contacts) == 0:
        print("В телефоном справочнике нет данных")
    for contact in contacts:
        print(i, contact.strip().split(';'))
        i += 1


# Функция Создать контакт
def create_contacts():
    name = input('Введите Имя:')
    last_name = input('Введите Фамилию:')
    number = input('Введите Телефон:')
    comment = input('Введите Комментарий:')
    string_in = ";".join([name, last_name, number, comment]) + '\n'
    phone_book = read_file()
    phone_book.append(string_in)
    save_file(phone_book)
    print('Запись', string_in, 'добавлена')


# Функция Изменить контакт
def edit_contact():
    # Читаем файл
    phone_book = read_file()
    # Проверяем есть ли в файле данные
    if len(phone_book) == 0:
        print("В телефоном справочнике нет данных")
    else:
        show_all_contacts()
        input_num = int(input('Введите порядковый номер контакта, который надо изменить: '))
        row = phone_book[input_num - 1].strip().split(';')
        name = input('Текущее Имя ' + row[0] + ' Введите Новое Имя:')
        last_name = input('Текущая Фамилия ' + row[1] + ' Введите Новую Фамилию:')
        number = input('Текущий Телефон ' + row[2] + ' Введите Новый Телефон:')
        comment = input('Текущий Комментарий ' + row[3] + ' Введите Новый Комментарий:')
        string_in = ";".join([name, last_name, number, comment]) + '\n'
        phone_book[input_num - 1] = string_in
        save_file(phone_book)
        print('Запись Номер ', input_num, 'изменена', string_in)


# Функция Удалить контакт
def delete_contacts():
    # Читаем файл
    phone_book = read_file()
    # Проверяем есть ли в файле данные
    if len(phone_book) == 0:
        print("В телефоном справочнике нет данных")
    else:
        show_all_contacts()
        input_num = int(input('Введите порядковый номер контакта, который надо удалить: '))
        del_string = phone_book.pop(input_num - 1)
        save_file(phone_book)
        print('Запись Номер ', input_num, 'удалена', del_string)


# Функция Найти контакт
def find_contact():
    # Читаем файл
    phone_book = read_file()
    # Проверяем есть ли в файле данные
    if len(phone_book) == 0:
        print("В телефоном справочнике нет данных")
    else:
        search_str = input('Введите фамилию или имя, которые надо найти: ')
        i = 1
        for contact in phone_book:
            data = contact.strip().split(';')
            if (search_str in data[0]) or (search_str in data[1]):
                print('Найдена запись Номер ', i, contact)
            else:
                print('Ни одна запись не найдена')
                break
            i += 1


# Функция Выход
def exit_func():
    print("Программа завершается")
    exit()


# Функция главного меню
def main_menu():
    print("\nТелефонный справочник\n")
    print("1. Показать все контакты")
    print("2. Создать контакт")
    print("3. Изменить контакт")
    print("4. Удалить контакт")
    print("5. Найти контакт")
    print("6. Выход")
    choice = input("Введите номер команды: ")
    if choice == "1":
        show_all_contacts()
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "2":
        create_contacts()
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "3":
        edit_contact()
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "4":
        delete_contacts()
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "5":
        find_contact()
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "6":
        exit_func()
    else:
        print("Введите правильную команду \n")
        enter = input("Press Enter to continue ...")
        main_menu()


# Вызываем функцию меню
main_menu()
