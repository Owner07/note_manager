username_in =input('Как тебя зовут?')
username=('Имя пользователя: ' + username_in)
subtitles =  [input("Введите название заметки: "),] # ввод первой заметки
while True:  # Бесконечный цикл при выполнении условия
    subtitles2 = input("Введите название заметки, что бы добавить еще заметку или оставьте поле пустым для перехода к следующему пункту меню: ")
    subtitles.append(subtitles2) # добавление в список subtitles следующих заголовков
    if not subtitles2: # окончание условия через пустой ввод
        break # окончание условия тру
        # elif subtitles2 not in subtitles: не получилось реализовать нейтрализацию одинаковых заголовков, почему то выдает ошибку

lastsubtitles ='Название заметки: ' + subtitles[-2]
content_in = input('Добавьте заметку: ')
content = ('Заметка: '+ content_in)
status_in = input('Введите важность заметки: ')
status = ('Статус заметки: '+ status_in)
created_date_in =input('Введите дату в формате День-месяц-год, например 10-12-2024: ')
created_date = ('Дата создания заметки: '+created_date_in[0:5])
issue_date_in = input('Введите дату окончания заметки в формате День-месяц-год, например 10-12-2025:')
issue_date = ('Дата истечения заметки: '+ issue_date_in[0:5]) # нужно поставить запрет на неверныый ввод даты

note = [

username,

lastsubtitles,

content,

status,

created_date,

issue_date,

'Список заголовков заголовки: ',

*subtitles # вложенный список для заголовков

]
print(*note, sep = '\n') # реализация вывода на новую строку

