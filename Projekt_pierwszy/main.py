tablica_ksiazek = []


def ShowMenu():
    print("___________MENU______________")
    print("1.Wybierz książkę")
    print("2.Wypożycz książkę")
    print("0.Wyjdź")

    choice = int(input("Wybierz\n"))
    if choice == 1:
        Show_Books()
    elif choice == 2:
        Rent_A_book(input("Wybierz numer książki"))
        return 2
    else:
        return 0


def Show_Books():
    tablica_ksiazek.clear()
    number = 1
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/books.txt", "r")
    x = file.readlines()
    for y in x:
        print(str(number) + ". " + y)
        tablica_ksiazek.append([number, y])
        number += 1


def Rent_A_book(number):
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/books.txt", "r")
    x = file.readlines()

    for y in x:
        if tablica_ksiazek[0] == number:
            print(tablica_ksiazek[1])
            break


while (True):
    ShowMenu()

