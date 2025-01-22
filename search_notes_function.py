
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def i(date):
    return datetime.strptime(date['issue_date'], '%d-%m-%Y')


def display_note(note, index):
    """Выводит информацию о заметке."""
    print(Fore.BLUE + f"\nЗаметка №{index}:" + Style.RESET_ALL)
    print(Fore.MAGENTA + "    Имя:" + Style.RESET_ALL, note['username'])
    print(Fore.MAGENTA + "    Заголовок:" + Style.RESET_ALL, note['title'])
    print(Fore.MAGENTA + "    Описание:" + Style.RESET_ALL, note['content'])
    print(Fore.MAGENTA + "    Статус:" + Style.RESET_ALL, note['status'])
    print(Fore.MAGENTA + "    Дата создания:" + Style.RESET_ALL, note['created_date'])
    print(Fore.MAGENTA + "    Дедлайн:" + Style.RESET_ALL, note['issue_date'])


def check_keyword_in_note(note, keyword):
    # проверка содержится ли поисковое слово в username, title или content заметки
    return (keyword in note["username"].lower() or
            keyword in note["title"].lower() or
            keyword in note["content"].lower())


def search_notes(notes, keyword=None, status=None):

    if not notes:
        print(Fore.RED + "Список заметок пуст." + Style.RESET_ALL)
        return []

    found_notes = []
    if not keyword:
        keyword = ""
    if not status:
        status = ""
    keyword = keyword.lower()
    status = status.lower()
    for i, note in enumerate(notes):
        if keyword and status:
            if check_keyword_in_note(note, keyword) and status == note["status"].lower():
                found_notes.append(note)
                display_note(note, i)
        elif keyword:
            if check_keyword_in_note(note, keyword):
                found_notes.append(note)
                display_note(note, i)
        elif status:
            if status == note["status"].lower():
                found_notes.append(note)
                display_note(note, i)

    if not found_notes and (keyword or status):
        print(Fore.RED + "\nЗаметки, соответствующие запросу, не найдены." + Style.RESET_ALL)

    return found_notes


# Пример использования:
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



