# Список для хранения заметок
notes = [
    {"username": "Матвей", "title": "Первая заметка", "content": "Первая заметка."},
    {"username": "Анна", "title": "Вторая заметка", "content": "Любимые блюда."},
    {"username": "Кристина", "title": "Список покупок", "content": "Молоко, колбаска."},
    {"username": "Артем", "title": "Любимые авто", "content": "Запорожец, Лада."}
]
print("Список заметок:\n")
        # Обращение по переменной idx
for idx, note in enumerate(notes):
    print(
        f"{idx + 1}. Имя: {note['username']}, Заголовок: {note['title']},\n Описание: {note['content']}\n")

def delete_notes():
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

# Запуск функции удаления заметок
delete_notes()