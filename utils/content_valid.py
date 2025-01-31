def content_valid():
    while True:
        content = input("Запишите заметку: ").strip()
        if content:
            return content
        else:
            print("Поле заметки не может быть пустым, пожалуйста заполните его: ")