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

def sort_name():
    with open("person_list.txt", "r") as file:
        stroka3 = file.readlines()
        array3 = []
        for stroka in stroka3:
            a = stroka.split(",")
            array3.append(a)
        array3 = sorted(array3, key = lambda x: x[1]) 
        
        stroka4 = ""
        for person in array3:
            data = ",".join(person)
            stroka4 += data + '\n'
        
    with open("person_list.txt", "w") as file:
        file.write(stroka4)
        


def sort_id():
    with open("person_list.txt", "r") as file:
        stroka5 = file.readlines()
        array5 = []
        for stroka in stroka5:
            a = stroka.split(",")
            array5.append(a)
        array5 = sorted(array5, key = lambda x: x[0]) 
        
        stroka6 = ""
        for person in array5:
            data = ",".join(person)
            stroka6 += data + '\n'
        
    with open("person_list.txt", "w") as file:
        file.write(stroka6)