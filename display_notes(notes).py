
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)  # автоматический сброс цвета

def i(date):
    return datetime.strptime(date['issue_date'], '%d.%m.%Y')

def display_notes(notes):
    if not notes:
        print(Fore.YELLOW + 'У вас нет сохраненных заметок!' + Style.RESET_ALL,Fore.LIGHTYELLOW_EX)
        return
    print(Fore.GREEN + '\nСписок сохраненных заметок: ' + Style.RESET_ALL)
    print(Fore.CYAN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Style.RESET_ALL)
    for num, note in enumerate(notes, 1):
        print(Fore.BLUE + f'\t\tЗаметка №{num}' + Style.RESET_ALL)
        print(Fore.MAGENTA + 'Имя пользователя:' + Style.RESET_ALL,Fore.GREEN + note['username'])
        print(Fore.MAGENTA + 'Заголовок:' + Style.RESET_ALL,Fore.GREEN + note['title'])
        print(Fore.MAGENTA + 'Описание:' + Style.RESET_ALL,Fore.GREEN + note['content'])
        print(Fore.MAGENTA + 'Статус:' + Style.RESET_ALL,Fore.GREEN + note['status'])
        print(Fore.MAGENTA + 'Дата создания:' + Style.RESET_ALL,Fore.GREEN + note['created_date'])
        print(Fore.MAGENTA + 'Дедлайн:' + Style.RESET_ALL,Fore.GREEN + note['issue_date'])
        print(Fore.CYAN + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Style.RESET_ALL)
        if not num % 5:
            input('Ввод для продолжения')


if __name__ == "__main__":
    notes = []  #
    display_notes(notes)

    input('Ввод для продолжения')
    notes.append({
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27.11.2024',
        'issue_date': '30.11.2024' # метод добавляет 1 элемент в конец списка
    })
    display_notes(notes)
    input('Ввод для продолжения')
    notes.extend([
        {
            'username': 'Мария',
            'title': 'Учеба',
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '10.08.2024',
            'issue_date': '18.07.2026'
        },
        {
            'username': 'Ирина Витальевна',
            'title': 'Хобби',
            'content': 'Купить картошку',
            'status': 'новая',
            'created_date': '12.09.2024',
            'issue_date': '25.11.2028' # метод добавляет сразу несколько элементов
        }
    ])
    notes.sort(key=i) #
    display_notes(notes)

    input('Ввод для продолжения')
    # большой массив данных
    display_notes(notes*10) # Копируем наш список на 10