i = 0;
while (True):

    student = input("ФИО студента: ")
    age = int(input("Возраст: "))
    gender = input("Укажите гендер: ")

    speciality = input("Назовите Специальность!");
    if speciality == "Computer Science":
        print(student)
        print(age)
        print(gender)
        break
    elif speciality != "":
        print("Такой специальности не существует! Повторите попытку еще раз")
    else:
        print("404 студент не найден!")

    i += 1