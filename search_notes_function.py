
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def display_note(note, index):
    print(Fore.BLUE + f"\nЗаметка №{index}:" + Style.RESET_ALL)
    print(Fore.MAGENTA + "    Имя:" + Style.RESET_ALL, note['username'])
    print(Fore.MAGENTA + "    Заголовок:" + Style.RESET_ALL, note['title'])
    print(Fore.MAGENTA + "    Описание:" + Style.RESET_ALL, note['content'])
    print(Fore.MAGENTA + "    Статус:" + Style.RESET_ALL, note['status'])
    print(Fore.MAGENTA + "    Дата создания:" + Style.RESET_ALL, note['created_date'])
    print(Fore.MAGENTA + "    Дедлайн:" + Style.RESET_ALL, note['issue_date'])  # функция вывода найденных заметок





def search_notes(notes, keyword=None, status=None):
    if not notes:
        print(Fore.RED + "Список заметок пуст." + Style.RESET_ALL)
        return []

    found_notes = []
    note_counter = 1  # Инициализируем счетчик для нумерации найденных заметок

    for note in notes:
        keyword_match = True
        if keyword is not None:
            keyword_match = (
                    keyword.lower() in note.get("username", "").lower()
                    or keyword.lower() in note.get("title", "").lower()
                    or keyword.lower() in note.get("content", "").lower()
            )

        status_match = True
        if status is not None:
            status_match = note.get('status').lower() == status.lower()  # Добавляем обработку отсутствия status

        if keyword_match and status_match:
            found_notes.append(note)
            display_note(note, note_counter)  # Используем счетчик найденных заметок
            note_counter += 1

    if not found_notes and (keyword or status):
        print(Fore.RED + "\nЗаметки, соответствующие запросу, не найдены." + Style.RESET_ALL)

    return found_notes


if __name__ == "__main__":
    notes = [
        {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты на неделю",
            "status": "новая",
            "created_date": "27-11-2024",
            "issue_date": "30-11-2024"
        },
        {
            "username": "Мария",
            "title": "Учеба",
            "content": "Подготовиться к экзамену",
            "status": "в процессе",
            "created_date": "25-11-2024",
            "issue_date": "01-12-2024"
        },
        {
            "username": "Иван",
            "title": "План работы",
            "content": "Завершить проект",
            "status": "выполнено",
            "created_date": "20-11-2024",
            "issue_date": "26-11-2024"
        }
    ]



    print(Fore.GREEN + "\nПримеры поиска:" + Style.RESET_ALL)
    print("\nПоиск по статусу 'новая'")
    search_notes(notes, status='новая')
    input()

    print("\nПоиск по слову 'купи'")
    search_notes(notes, keyword='купи')
    input()

    print("\nПоиск по слову 'учеба' и статусу 'в процессе'")
    search_notes(notes, keyword='учеба', status='в процессе')



