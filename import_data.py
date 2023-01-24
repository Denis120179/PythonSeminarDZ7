def add_data():
    id = input("Введите id:  ")
    first_name = input("Введите имя:  ")
    last_name = input("Введите фамилию:  ")
    nomber_phone = input("Введите номер телефона:  ")
    comment = input("Введите комментарий:  ")
    stroka = f"{id}, {first_name}, {last_name}, {nomber_phone}, {comment} \n"
    with open("person_list.txt", "a") as file:
        file.write(stroka)
    print("Данные введены корректно и сохранены")