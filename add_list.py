username =input('Как тебя зовут?')
print('Имя пользователя: ' + username)
subtitles =  ['Основные темы','Персонажи','Рекомендации для чтения']
title = input('Введите название заметки: ')
subtitles.append(title)
print(subtitles)
content = input('Добавьте заметку: ')
print('Описание заметки: '+ content)
status = input('Введите важность заметки: ')
print('Статус заметки: '+ status)
created_date =input('Введите дату в формате День-месяц-год, например 10-12-2024: ')
print('Дата создания заметки: '+created_date[0:5])
issue_date = input('Введите дату окончания заметки в формате День-месяц-год, например 10-12-2025:')
print('Дата истечения заметки: '+ issue_date[0:5])