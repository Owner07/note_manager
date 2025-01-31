def title_valid():
    while True:
        title = input("Введите название заметки: ").strip()
        if title:
            return title
        else:
            print("Название заметки не может быть пустым, пожалуйста введите название заметки: ")
