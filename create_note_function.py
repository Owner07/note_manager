from datetime import datetime, timedelta


def valid_name():
    while True:
        name = input("Введите имя пользователя: ").strip()
        if name:
            return name
        else:
            print("Имя не может быть пустым, пожалуйста введите настоящее имя: ")
def title_valid():
    while True:
        title = input("Введите название заметки: ").strip()
        if title:
            return title
        else:
            print("Название заметки не может быть пустым, пожалуйста введите название заметки: ")
def content_valid():
    while True:
        content = input("Запишите заметку: ").strip()
        if content:
            return content
        else:
            print("Поле заметки не может быть пустым, пожалуйста заполните его: ")

statuses = ['новая', 'в работе', 'завершена']  # Возможные статусы заметок

def status_valid():
    while True:
        status = input("Введите статус заметки (например, 'новая', 'в работе', 'завершена'): ").strip().lower()
        if status in statuses:
            print(f"Статус заметки: {status}")
            return status # Выходим из цикла, если статус корректен
        else:
            print("Некорректный статус. Пожалуйста, выберите из предложенных: 'новая', 'в работе', 'завершена'")
def issue_date_valid():
    while True:
        issue_date = input("Введите дату дедлайна в формате ДД.ММ.ГГГГ, например 12.12.2025 или нажмите '1' для окончания даты через неделю: ").strip()
        if issue_date == "1":
            issue_date = datetime.now() + timedelta(days=7)
            return issue_date.strftime('%d.%m.%Y')
        else:
            try:
                datetime.strptime(issue_date, '%d.%m.%Y')
                return issue_date
            except ValueError:
                print("Вы ввели не верный формат даты, введите дату дедлайна в формате ДД.ММ.ГГГГ, например 12.12.2025: ")



def create_note():
    created_date = datetime.now().strftime('%d.%m.%Y')
    print("Текущая дата: " + created_date)

    name = valid_name()
    title = title_valid()
    content = content_valid()
    status = status_valid()
    issue_date = issue_date_valid()

    note = {
        'Имя пользователя: ': name,
        'Заголовок: ': title,
        'Заметка: ': content,
        'Статус заметки: ': status,
        'Дата создания: ': created_date,
        'Дедлайн: ': issue_date
}

    return note
new_create = create_note()

for key, items in new_create.items():
    print(f"{key} {items}")

