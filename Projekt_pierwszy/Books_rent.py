def Rent_A_book(imie):
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/users.txt","r")

    x = file.readlines()
    for y in x:
        imiona =  y.split(" ")
        if imiona[0] == imie:
            print("Znaleziono")
            break

Rent_A_book(input("Wprowadź imię\n"))