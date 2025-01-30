from datetime import datetime, timedelta
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def i(date):
    return datetime.strptime(date['issue_date'], '%d.%m.%Y')

def menu():
    while True:
        print(Fore.GREEN +"\nМеню:",
              Fore.MAGENTA +"\n1. Создать новую заметку",
              Fore.MAGENTA + "\n2. Показать все заметки",
              Fore.MAGENTA +"\n3. Обновить заметку",
              Fore.MAGENTA + "\n4. Удалить заметку",
              Fore.MAGENTA +"\n5. Найти заметки",
              Fore.MAGENTA +"\n6. Выйти из программы")
        item_menu = input(Fore.LIGHTYELLOW_EX + "Укажите пункт меню: ")
        if item_menu.isdigit() and int(item_menu) in range(1, 7):
            return int(item_menu)
        else:
            print(Fore.RED +"\nНеверный выбор. Пожалуйста, выберите действие из списка.")

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

statuses = ['новая', 'в работе', 'завершена']

def status_valid():
    while True:
        status = input("Введите статус заметки (например, 'новая', 'в работе', 'завершена'): ").strip().lower()
        if status in statuses:
            print(f"Статус заметки: {status}")
            return status
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
    print(Fore.YELLOW + "Текущая дата: " + created_date)

    name = valid_name()
    title = title_valid()
    content = content_valid()
    status = status_valid()
    issue_date = issue_date_valid()

    note = {
        Fore.LIGHTYELLOW_EX + 'username': Fore.BLUE + name,
        Fore.LIGHTYELLOW_EX + 'title': Fore.BLUE + title,
        Fore.LIGHTYELLOW_EX + 'content': Fore.BLUE + content,
        Fore.LIGHTYELLOW_EX + 'status':Fore.BLUE + status,
        Fore.LIGHTYELLOW_EX + 'created_date':Fore.BLUE + created_date,
        Fore.LIGHTYELLOW_EX + 'issue_date':Fore.BLUE + issue_date
    }
    return note

def display_note(note, index):
   print(Fore.BLUE + f"\nЗаметка №{index + 1}:" + Style.RESET_ALL)
   print(Fore.MAGENTA + "    Имя:" + Style.RESET_ALL, note['username'])
   print(Fore.MAGENTA + "    Заголовок:" + Style.RESET_ALL, note['title'])
   print(Fore.MAGENTA + "    Описание:" + Style.RESET_ALL, note['content'])
   print(Fore.MAGENTA + "    Статус:" + Style.RESET_ALL, note['status'])
   print(Fore.MAGENTA + "    Дата создания:" + Style.RESET_ALL, note['created_date'])
   print(Fore.MAGENTA + "    Дедлайн:" + Style.RESET_ALL, note['issue_date'])


def show_all_notes(notes):
    if not notes:
        print(Fore.RED + "Список заметок пуст." + Style.RESET_ALL)
        return
    else:
        print(Fore.GREEN + "\nСписок заметок:" + Style.RESET_ALL)
        for i, note in enumerate(notes, 1):
            display_note(note, i)

def update_note(notes):
    if not notes:
         print(Fore.RED + "Список заметок пуст." + Style.RESET_ALL)
         return

    show_all_notes(notes) # Вывод списка заметок

    while True:
          try:
              note_number = int(input("Введите номер заметки, которую хотите обновить (или '0' для отмены): "))
              if note_number == 0:
                print("Отмена обновления.")
                return
              elif 1 <= note_number <= len(notes):
                  note_index = (note_number - 1)
                  note = notes[note_index]
                  break # если ввод корректный, выходим из цикла
              else:
                  print("Некорректный номер заметки. Попробуйте снова.")
          except ValueError:
                print("Некорректный ввод, введите целое число.")


    change_status = input("Хотите изменить данные текущей заметки? (да/нет): ").lower().strip()
    if change_status == 'да':
        while True:
            change_value = input("Выберите название поля, которое хотите заменить (или оставьте поле пустым для завершения): ").strip().lower()
            if change_value == '':
               break # Выходим из цикла, если пользователь ввел пустой ввод

            if change_value == 'username':
                note['username'] = input("Введите новое имя пользователя: ")
            elif change_value == 'title':
                note['title'] = input("Введите новое название заметки: ")
            elif change_value == 'content':
                note['content'] = input("Введите новое содержание заметки: ")
            elif change_value == 'status':
               note['status'] = input("Введите новый статус заметки: ")
            elif change_value == 'issue_date':
                while True:
                    new_issue_date = input("Введите новую дату дедлайна в формате ДД.ММ.ГГГГ: ")
                    try:
                        datetime.strptime(new_issue_date, '%d.%m.%Y')
                        note['issue_date'] = new_issue_date
                        break  # Выходим из внутреннего цикла, если дата введена верно
                    except ValueError:
                       print("Неверный формат даты. Попробуйте снова.")
            elif change_value == 'created_date':
                  print("Поле 'created_date' не может быть изменено")
            else:
                 print("Неверное название поля. Попробуйте снова.") # обработка неверного ввода

        print("Новые данные заметки: ")
        display_note(note,note_index)

    else:
        print("Изменения не внесены!")

def delete_notes(notes):
    show_all_notes(notes)
      # Запрос у пользователя имя пользователя или заголовок заметки
    search_term = input("Введите имя пользователя или заголовок заметки для удаления: ").strip()
    if not notes:
        print("Список заметок пуст.")
        return

    # Флаг для отслеживания, о нахождение заметок
    found = False

    # Проходим по списку заметок
    for note in notes[:]:  # Используем срез, создать копию и чтобы менять список в процессе итерации
        if search_term == note["username"].strip() or search_term == note["title"].strip(): # == оператор использован что бы функция не срабатывала на часть слова
            # Подтверждение удаления
            confirm = input(f"Вы уверены, что хотите удалить заметку '{note['title']}', "
                            f"Пользователя  {note['username']} "
                            f"(да/нет)? ").strip().lower()
            if confirm == 'да':
                notes.remove(note)
                print(f"Заметка '{note['title']}', "
                      f"Пользователя  '{note['username']}' успешно удалена.")
                found = True

    if not found:
        print("Заметка не удалена.")

    # Вывод обновлённого списка заметок
    print("Обновленный список заметок:")
    for note in notes:
        print(f"{note['username']} - {note['title']}: {note['content']}")

def check_keyword_in_note(note, keyword):
    return (keyword.lower() in note["username"].lower() or
            keyword.lower() in note["title"].lower() or
            keyword.lower() in note["content"].lower())

def search_notes(notes, keyword=None, status=None):

    if not notes:
        print(Fore.RED + "Список заметок пуст." + Style.RESET_ALL)
        return []

    found_notes = []
    if not keyword:
        keyword = ""
    if not status:
        status = ""
    keyword = keyword.lower().strip()
    status = status.lower().strip()  # перевод в нижний регистр и устранение пробелов если бы был инпут
    for i, note in enumerate(notes): # нумерация заметок
        if keyword and status:
            if check_keyword_in_note(note, keyword) and status == note["status"].lower():
                found_notes.append(note)
                display_note(note, i) # сначала поиск самого сложного варианта по 2 значениям
        elif keyword:
            if check_keyword_in_note(note, keyword):
                found_notes.append(note)
                display_note(note, i) # поиск по слову
        elif status:
            if status == note["status"].lower().strip():
                found_notes.append(note)
                display_note(note, i) # поиск по статусу

    if not found_notes and (keyword or status):
        print(Fore.RED + "\nЗаметки, соответствующие запросу, не найдены." + Style.RESET_ALL)

    return found_notes
# Основной цикл программы
if __name__ == "__main__":
    notes = []  # Список для хранения заметок

    while True:
        choice = menu()

        if choice == 1:
           new_note = create_note()
           notes.append(new_note)
           print(Fore.YELLOW + "\nСоздана новая заметка:")
           for key, value in new_note.items():
             print(f"{key}: {value}")
        elif choice == 2:
           show_all_notes(notes)
        elif choice == 3:
            update_note(notes)
        elif choice == 4:
            delete_notes(notes)
        elif choice == 5:
            keyword = input(Fore.LIGHTYELLOW_EX +"Введите ключевое слово для поиска (оставьте пустым, если не нужно): ").strip()
            status = input(Fore.LIGHTYELLOW_EX +"Введите статус для поиска (оставьте пустым, если не нужно): ").strip()
            search_notes(notes, keyword, status)
        elif choice == 6:
           print("Выход из программы.")
           break
