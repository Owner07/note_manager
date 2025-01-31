from datetime import datetime
import utils

def create_note():
    created_date = datetime.now().strftime('%d.%m.%Y')
    name = utils.valid_name()
    title = utils.title_valid()
    content = utils.content_valid()
    status = utils.status_valid()
    issue_date = utils.issue_date_valid()

    note = {
        'Имя пользователя': name,
        'Заголовок': title,
        'Заметка': content,
        'Статус заметки': status,
        'Дата создания': created_date,
        'Дедлайн': issue_date
    }
    return note

new_create = create_note()

for key, items in new_create.items():
    print(f"{key}: {items}")