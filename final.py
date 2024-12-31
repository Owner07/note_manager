username_in =input('Как тебя зовут?')
username=('Имя пользователя: ' + username_in)
subtitles =  ['Основные темы','Персонажи','Рекомендации для чтения']
title = input('Введите название заметки: ')
subtitles.append(title)
content_in = input('Добавьте заметку: ')
content = ('Описание заметки: '+ content_in)
status_in = input('Введите важность заметки: ')
status = ('Статус заметки: '+ status_in)
created_date_in =input('Введите дату в формате День-месяц-год, например 10-12-2024: ')
created_date = ('Дата создания заметки: '+created_date_in[0:5])
issue_date_in = input('Введите дату окончания заметки в формате День-месяц-год, например 10-12-2025:')
issue_date = ('Дата истечения заметки: '+ issue_date_in[0:5])

note = [

username,

content,

status,

created_date,

issue_date,

subtitles # вложенный список для заголовков

]
print(note)