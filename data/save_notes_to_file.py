from datetime import datetime, timedelta
import yaml


def valid_name():
    while True:
        username = input("Введите имя пользователя.: ").strip()
        if username:
            return username
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
    print("Текущая дата - дата создания заметки: " + created_date)

    username = valid_name()
    title = title_valid()
    content = content_valid()
    status = status_valid()
    issue_date = issue_date_valid()

    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
        }

    return note





# Функция по сохранению заметок в файл в структурированном формате
def append_notes_to_file(notes, filename):
    with open(filename, mode="a", encoding="utf-8") as file:
        yaml_notes = notes  # Создаем копию списка словарей для дальнейшей работы
        for index in range(len(yaml_notes)): # Преобразуем ключи словарей в понятный для пользователя вид
            yaml_notes[index]["Имя пользователя"] = yaml_notes[index].pop("username")
            yaml_notes[index]["Заголовок"] = yaml_notes[index].pop("title")
            yaml_notes[index]["Описание"] = yaml_notes[index].pop("content")
            yaml_notes[index]["Статус"] = yaml_notes[index].pop("status")
            yaml_notes[index]["Дата создания"] = yaml_notes[index].pop("created_date")
            yaml_notes[index]["Дедлайн"] = yaml_notes[index].pop("issue_date")
        yaml.dump(yaml_notes, file, allow_unicode=True, sort_keys=False)


# Создаем первую заметку и добавляем в список
notes_list = [create_note()]
# Запрашиваем необходимость добавления новой заметки
while True:
    add_new_note = input("\nХотите добавить ещё одну заметку? (Да/Нет): ")
    if add_new_note.lower() == "нет":
        break
    elif add_new_note.lower() == "да":
        notes_list.append(create_note())
        continue
    else:
        print('Введите "Да" или "Нет"')
        continue

# Сохраняем созданные заметки в существующий файл
while True:
    request_append_new_note = input(f"\nХотите добавить новые заметки в файл? (Да/Нет): ")
    if request_append_new_note.lower() == "да":
        filename_ = input("Введите название существующего файла yaml: ") + ".yaml"
        try:
            append_notes_to_file(notes_list, filename_)
        except  FileNotFoundError:
            print(f"\nФайл {filename_} не найден. Создан новый файл.")
            open(filename_, mode="x")
            append_notes_to_file(notes_list, filename_)
        except UnicodeDecodeError:
            print(f"\nОшибка при чтении файла {filename_}. Проверьте его содержимое.")
        except PermissionError:
            print(f"\nДоступ к файлу {filename_} запрещен.")
        break
    elif request_append_new_note.lower() == "нет":
        print('Файл не создан')
        break
    else:
        print('Введите "Да" или "Нет"')
        continue
