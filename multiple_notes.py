from datetime import datetime


def is_valid_date(date_string):
    # Проверка на валидность формата даты
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def get_valid_name():
    # Запрашивает имя пользователя и возвращает его, пока оно не будет валидным.
    while True:
        name = input("Введите имя пользователя: ").strip()
        if name:
            return name
        else:
            print("Имя не может быть пустым!")

def get_valid_title():
    while True:
        title = input("Введите заголовок заметки: ").strip()
        if title:
            return title
        else:
            print("Заголовок не может быть пустым!")  # Проверка пустого заголовка
def get_description_valid():
    while True:
        description = input("Введите описание заметки: ").strip()
        if description:
            return description
        else:
            print("Описание не может быть пустым!") # Проверка пустого описания

def create_note():
    # Создание заметки и возврат словаря с заметкой
    name = get_valid_name()  # Получаем корректное имя с помощью функции
    title = get_valid_title() # выапвыап
    description = get_description_valid()


    statuses = ['новая', 'в работе', 'завершена']  # Возможные статусы заметок

    while True:
        status = input("Введите статус заметки (например, 'новая', 'в работе', 'завершена'): ").strip().lower()
        if status in statuses:
            print(f"Статус заметки: {status}")
            break  # Выходим из цикла, если статус корректен
        else:
            print("Некорректный статус. Пожалуйста, выберите из предложенных: 'новая', 'в работе', 'завершена'")

    creation_date = input("Введите дату создания (дд.мм.гггг): ").strip()

    # Проверка на корректность даты
    while not is_valid_date(creation_date):
        print("Некорректный формат даты. Пожалуйста, введите дату в формате дд-мм-гггг.")
        creation_date = input("Введите дату создания (дд.мм.гггг): ").strip()

    deadline = input("Введите дедлайн (дд-мм-гггг): ").strip()

    # Проверка на корректность дедлайна
    while not is_valid_date(deadline):
        print("Некорректный формат даты. Пожалуйста, введите дедлайн в формате дд-мм-гггг.")
        deadline = input("Введите дедлайн (дд-мм-гггг): ").strip()

    note = {
        'name': name,
        'title': title,
        'description': description,
        'status': status,
        'creation_date': creation_date,
        'deadline': deadline
    }

    return note


def display_notes(notes):
    # Отображение всех заметок
    if not notes:
        print("Нет созданных заметок.")
        return

    print("Список заметок:\n")
    for idx, note in enumerate(notes):
        print(
            f"{idx + 1}. Имя: {note['name']}, Заголовок: {note['title']}, Описание: {note['description']},"
            f" Статус: {note['status']}, Дата создания: {note['creation_date']}, Дедлайн: {note['deadline']}\n")

def main():
    notes = []
    print("Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.")

    while True:
        user_input = input("Введите 'добавить' для создания заметки, 'стоп' для завершения работы: ").strip().lower()

        if user_input == 'стоп':
            break  # Завершаем, если ввели 'стоп'
        elif not user_input:
            break  # Завершаем, если пустой ввод
        elif user_input == 'добавить':
            note = create_note()
            if note:
                notes.append(note)
                print("Заметка добавлена.")
                another_note = input("Хотите добавить еще одну заметку? (да/нет): ").strip().lower()
                if another_note != 'да':
                    break  # Завершаем, если пользователь не хочет добавлять еще заметку ( не смог сделать без вывода строки "Введите 'добавить' для создания заметки, 'стоп' для завершения работы: " после ответа "да"
        else:
            print("Некорректная команда, попробуйте снова.")

    display_notes(notes)


if __name__ == "__main__":
    main()