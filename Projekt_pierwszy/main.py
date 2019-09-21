tablica_ksiazek = []
users = []

def Login():
    login = input(" Podaj login")
    haslo = input(" Podaj hasło")
    return login,haslo

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

    for y in tablica_ksiazek:
        if y[0] == int(number):
            print(y[1])
            break
def Logowanie():
    login, haslo = Login()
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/users.txt", "r")
    x = file.readlines()
    for y in x:
        u = y.split(" ")
        if u[0] == login:
            if u[1] == haslo:
                print("poprawnie zalogowano!")
                return 1
    print("Niesetty nie udało ci się zalogować")
    return 0
while (True):
    if Logowanie() == 1:
        pass
    else:
        break
    ShowMenu()

