def valid_name():
    while True:
        name = input("Введите имя пользователя: ").strip()
        if name:
            return name
        else:
            print("Имя не может быть пустым, пожалуйста введите настоящее имя: ")