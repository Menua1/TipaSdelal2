import model
import view


# Функция просмотра всех контактов 
def all_contacts(count: int = 0) -> list:
    reference, status = model.get_reference(count)
    if status:
        print("Успешно")
    #     view.display_message("Записи успешно извлечены")
    # else:
    #     view.display_error("Ошибка: количество записей меньше запрошенного")
    return reference

# Функция откртия файла
def opening_file(file_name: str = "test.txt") -> list:
    reference, status = model.read_reference_from_file(file_name)
    if status:
        print("Успешно")
    #     view.display_message(
    #         "Контакт из файла {} выполнено успешно".format(file_name))
    # else:
    #     view.display_error(
    #         "Ошибка чтения контакта из файла: {}".format(file_name))
    return reference

# Функция записи контакта в файл
def directory_entry(file_name: str, reference: list) -> bool:
    status = model.write_reference_from_file(file_name, reference)
    if status:
        print("Успешно")
    #     view.display_message(
    #         "Контакт, записанный в файл {} выполнено успешно".format(file_name))
    # else:
    #     view.display_error(
    #         "Ошибка записи контакта на файл: {}".format(file_name))

# Функция добавления нового контакта
def add_contact(record: dict) -> (list):
    reference, status = model.add_reference(record)
    if status:
        print("Успешно")
    #   view.display_error(
    #       "Добавить элемент не удалось: {}".format(reference))
    # else:
    #   view.display_message("Элемент успешно добавлен")
    return reference, status




# Функция удаления контакта
def delete_contact(id: int) -> list:
    reference, status = model.delete_reference(id)
    if status:
        print("Успешно")
    #   view.display_message("Контак с id {} успешно удаление".format(id))
    # else:
    #   view.display_error("Ошибка удаления контакта с id {}: элемент не найден".format(id))
    return reference

# Функция обновления контакта
def update_contact(id: int, record: dict) -> list:
    reference, status = model.update_reference(id, record)
    if status:
        print("Успешно")
    #   view.display_message("Контак с id {} успешно обновлен".format(id))
    # else:
    #   view.display_error("Ошибка обновления контакта с id {}: элемент не найден".format(id))
    return reference

# Функция нахождения в справочнике контакта с указанными параметрами
def find_contact(parameters: dict = {}) -> list:
    reference, status = model.find_records(parameters)
    if status:
        print("Успешно")
    #     view.display_message("Запись найдена успешно")
    # else:
    #     view.display_error(
    #         "Ошибка поиска записи с параметрами {}: запись не найдена".format(parameters))
    return reference

# Функция нахождения в справочнике контакта по id
def search_id(id: int) -> list:
    reference, status = model.find_record_from_id(id)
    if status:
        print("Успешно")
    #   view.display_message("Запись с id {} успешно найдена".format(id))
    # else:
    #     view.display_error(
    #         "Ошибка поиска записи по id {}: запись не найдена".format(id))
    return reference

# Функция создания случайных записей
def random_entries(count: int = 10) -> list:
    imaginary_friends, status = model.generate_reference(count)
    if status:
        print()
    #   self.view.display_message("Ссылки сгенерированны успешно")
    # else:
    #   self.view.display_error("Ошибка генерации ссылок")
    return imaginary_friends


def input_handler(inp: int):
    if inp == 1:
        view.show_all(all_contacts()) # просмотра всех контактов
    elif inp == 2:
        view.db_success(opening_file('test.txt'))  # открыть файл
    elif inp == 3:
        directory_entry('test.txt', model.reference)  # сохранить контакт
    elif inp == 4:
        add_contact(view.create_contact())  # добавить контакт
    elif inp == 0:
        view.exit_program()  # выход


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
