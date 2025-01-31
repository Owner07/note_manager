from datetime import datetime, timedelta
def issue_date_valid():
    while True:
        issue_date = input("Введите дату дедлайна в формате ДД.ММ.ГГГГ, например 12.12.2025 или нажмите '1' для окончания даты через неделю: ").strip()
        if issue_date == "1":
            issue_date = datetime.now() + timedelta(days=7)
            return issue_date.strftime('%d.%m.%Y')
        else:
            try:
                datetime.strptime(issue_date, '%d.%m.%Y')
                return issue_date
            except ValueError:
                print("Вы ввели не верный формат даты, введите дату дедлайна в формате ДД.ММ.ГГГГ, например 12.12.2025: ")