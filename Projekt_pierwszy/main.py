tablica_ksiazek = []
users = []
login_cout = 3

def ShowMenu():
    print("___________MENU______________")
    print("1.Wybierz książkę")
    print("2.Wypożycz książkę")
    print("3.Wyświetl użytkowników")
    print("0.Wyjdź")

    choice = int(input("Wybierz\n"))
    if choice == 1:
        Show_Books()
    elif choice == 2:
        Rent_A_book(input("Wybierz numer książki"))
    elif choice == 3:
        create_user_table()
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


def create_user_table():
    users.clear()
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/users.txt", "r")
    x = file.readlines()

    for y in x:
        login, passw = y.split(" ")
        users.append([login, passw])
        print(y)


def Rent_A_book(number):
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/books.txt", "a")
    x = file.readlines()

    for y in tablica_ksiazek:
        if y[0] == int(number):
            print(y[1])

            break


def Logowanie():
    login = input(" Podaj login")
    haslo = input(" Podaj hasło")
    file = open("C:/Users/studentwsb/lab/Projekt_pierwszy/users.txt", "r")
    x = file.readlines()
    for y in x:
        u = y.split(" ")
        if u[0] == login:
            if u[1] == haslo:
                print("poprawnie zalogowano!")
                return 1
    return 0


while (True):
    l = Logowanie()
    if l == 1:
        if ShowMenu() == 0:
            break
        else:
            pass
    elif l == 0 and login_cout !=0:
        print("Spróbuj ponownie zostało " +str(login_cout)+ " prób logowania")
        login_cout -= 1
    else:
        print("Niesetty nie udało ci się zalogować")
        break

