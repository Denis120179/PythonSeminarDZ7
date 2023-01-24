def menu_action():
    action = int(input(
        "Выберите желаемое действие:\n 1 - ввод данных\n 2 - вывод данных\n 3 - сортировка\n 4 - выход\n"))
    if action == 2:
        action = int(input("5 - вывод данных полностью\n 6 - вывод имени и фамилии\n"))
    if action == 3:
        action = int(input("7 - сортировка по имени\n 8 - сортировка по id\n"))        
    return action 


