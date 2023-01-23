def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['1.Показать все контакты',
                 '2.Открыть файл',
                 '3.Сохранить файл',
                 '4.Создать контакт',
                 '5.Изменить контакт',
                 '6.Удалить контакт по id',
                 '7.Поиск контакта по id',
                 '8.Поиск по параметрам',
                 '0.Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду >: '))
    # TODO: сделать валидацию
    return user_input


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы.')
    n = int(input('Вы уверены что хотите выйти? \n 1.Да \n2.Нет \n'))
    if n == 2:
        return -1
    elif n == 1:
        exit()
    else:
        print('Введите что то выбраное из списка!')
    exit_program()


def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact


def change_cont(book):  # Изменение контакта
    index = poisk(book)
    if index != -1:
        print_num(book[index])
        if input('Вы уверены что хотите изменить контакт?\n 1 - Да, \n  2 - Нет\n') == '1':
            result_od = book[index]
            result = book[index].split(", ")
            vbr = input(
                'Выберите что изменить "Имя", "Фамилия", "Номер", "Комментарий":\n ')
            name = result[0]
            firstname = result[1]
            number = result[2]
            comment = result[3]
            rename = input('Что менять?:')
            if vbr.lower() == 'Новое имя':
                result.remove(name)
                result.insert(0, rename)
            elif vbr.lower() == 'Новая фамилия':
                result.remove(firstname)
                result.insert(1, rename)
            elif vbr.lower() == 'Новый номер':
                result.remove(number)
                result.insert(2, rename)
            elif vbr.lower() == 'Новый комментарий':
                result.remove(comment)
                result.insert(3, rename)
            else:
                print('Упс.Что то пошло не так!!!')
            print_num(result)
            print('\nКонтакт изменен!!!')
            return result, result_od
        else:
            print('\nКонтакт не изменен')
            return '', ''
    else:
        return '', ''


def delite_num(count: int):
    user_id = int(input('Введите id контакта для удаления: '))
    if user_id > 0 and user_id <= count:
        if input('Вы уверены что хотите удалить контакт?\n 1 - Да, \n  2 - Нет\n') == '1':
            return user_id - 1
            # print('Контакт удален')
    else:
        print('Неверный id контакта')


def print_num(book):
    print("-" * len(book))
    print(book)
    print("-" * len(book))


def poisk(book):
    ans = input(
        'Введите номер телефона или имя контакта:\n')
    for line in book:
        if ans.lower() in line.lower():
            return book.index(line)
    print('\nТакого контакта не существует,если хотите добавить выберите пункт 4 \n')
    return -1


def search_contact_by_id(count: int):
     user_id = int(input('Введите id контакта для удаления: '))
     if user_id > 0 and user_id <= count:
       return user_id - 1 # print('Контакт удален')
     else:
        print('Неверный id контакта')


def display_message(message: str):
  print(f'\033[31m{message}\033[0m')
