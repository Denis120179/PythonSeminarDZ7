def print_data():
    with open("person_list.txt", "r") as file:
        for stroka in file.readlines():
            print(stroka, end = "")

def print_name():
    with open("person_list.txt", "r") as file:
        stroka2 = file.readlines()
        for stroka in stroka2:
            a = stroka.split(",")
            print(f"{a[1]} {a[2]}")

#def sort_name():
#    with open("person_list.txt", "r") as file:
#        stroka3 = file.readlines()
#        stroka3 = sorted(stroka3.lambda x: x)
#    pass
        


#def sort_id():
#    pass
