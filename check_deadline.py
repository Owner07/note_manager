from datetime import datetime # импорт класса для работы с датами.

DATE_FORMAT = "%d.%m.%Y"  # Константа для формата даты


def get_deadline_date():
    # Запрашивает у пользователя дату дедлайна и возвращает объект datetime.
    while True:
        issue_date_in = input(f"Введите дату дедлайна в формате в формате ДД.ММ.ГГГГ: ")
        try:
            issue_date = datetime.strptime(issue_date_in, DATE_FORMAT)
            return issue_date
        except ValueError:
            print(f"Некорректный формат даты. Пожалуйста, используйте формат {DATE_FORMAT}.")


def склонять_день(days):
    # Склоняет слово "день" в зависимости от числа.
    if days == 1:
        return "день"
    elif 1 < days < 5:
      return "дня"
    else:
        return "дней"


def проверить_дедлайн():
    # Проверяет, истек ли дедлайн, и выводит результат.
    issue_date = get_deadline_date() # Вызываем функцию ввода даты

    now_date = datetime.now() # присваивает дату на момент запроса

    if issue_date < now_date:
        days_overdue = (now_date - issue_date).days
        print(f"Дедлайн истек на {days_overdue} {склонять_день(days_overdue)} назад.") # высчитываем разницу между датами
    else:
        days_remaining = (issue_date - current_date).days
        print(f"Дедлайн еще не истек. Осталось {days_remaining} {склонять_день(days_remaining)}.")  # высчитываем разницу между датами


проверить_дедлайн()