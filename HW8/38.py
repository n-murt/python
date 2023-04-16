# Функция Открыть файл
def open_file():
    try:
        file_o = open('phonebook.txt', 'r', encoding='utf-8')
    except IOError:
        file_o = open('phonebook.txt', 'w', encoding='utf-8')
        print('Файла нет, создаем пустой')
    return file_o


# Функция Сохранить файл
def save_file(file_o):
    return


# Функция Посмотреть все контакты
def show_all_contacts(file_o):
    i = 1
    contacts = file_o.readlines()
    if len(contacts) == 0:
        print("В телефоном справочнике нет данных")
    for contact in contacts:
        print(i, contact.strip().split(';'))
        i = +1


# Функция Создать контакт
def create_contacts(file_o):
    return


# Функция Найти контакт
def find_contact(file_o):
    return


# Функция Изменить контакт
def edit_contact(file_o):
    return


# Функция Удалить контакт
def delete_contacts(file_0):
    return


# Функция Выход
def exit_func(file_o):
    file_o.close()
    print("Программа завершается")
    exit()


# Функция главного меню
def main_menu():
    file_o = open_file()
    print("\nТелефоннный справочник\n")
    print("1. Показать все контакты")
    print("2. Создать контакт")
    print("3. Изменить контакт")
    print("4. Удалить контакт")
    print("5. Выход")
    choice = input("Введите номер команды: ")
    if choice == "1":
        show_all_contacts(file_o)
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "2":
        create_contacts(file_o)
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "3":
        edit_contact(file_o)
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "4":
        delete_contacts(file_o)
        user_input = input("Нажмите Enter для продолжения ...")
        main_menu()
    elif choice == "5":
        exit_func(file_o)
    else:
        print("Введите правильную команду \n")
        enter = input("Press Enter to continue ...")
        main_menu()
