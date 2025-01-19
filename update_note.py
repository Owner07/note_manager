from datetime import datetime


note = {'username: ': 'Алексей',
        'title: ': 'Список покупок',
        'content: ': 'Купить продукты на неделю',
        'status: ': 'новая',
        'created_date: ': '27-11-2024',
        'issue_date: ': '30-11-2024'
        }
print("Текущие данные заметки: ")
for key, items in note.items():
    print(f"{key} {items}")
def update_note():
    change_status = input("Хотите изменить данные текущей заметки? (да/нет): ").lower().strip()
    if change_status == 'да':
        while True:  # бесконечный цикл для повторного ввода
            change_value = input("Выберите название поля, которое хотите заменить (или оставьте поле пустым для завершения): ").strip().lower()

            if change_value == '':
               break # Выходим из цикла, если пользователь ввел пустой ввод

            if change_value == 'username':
                note['username: '] = input("Введите новое имя пользователя: ")
            elif change_value == 'title':
                note['title: '] = input("Введите новое название заметки: ")
            elif change_value == 'content':
                note['content: '] = input("Введите новое содержание заметки: ")
            elif change_value == 'status':
               note['status: '] = input("Введите новый статус заметки: ")
            elif change_value == 'issue_date: ':
                    while True:
                            new_issue_date = input("Введите новую дату дедлайна в формате ДД.ММ.ГГГГ: ") # что бы не срывался цикл из за неверной даты
                            try:
                                    datetime.strptime(new_issue_date, '%d.%m.%Y')
                                    note['issue_date: '] = new_issue_date
                                    break  # Выходим из внутреннего цикла, если дата введена верно
                            except ValueError:
                                    print("Неверный формат даты. Попробуйте снова.")
            elif change_value == 'created_date':
                  print("Поле 'created_date' не может быть изменено")
            else:
                 print("Неверное название поля. Попробуйте снова.") # обработка неверного ввода


    else:
        print("Изменения не внесены!")



update_note ()
print("Новые данные заметки: ")
for key, items in note.items():
    print(f"{key} {items}")