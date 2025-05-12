from utilis.model import users
from utilis.controller import get_user_info, add_user, remove_user


def main():
    while True:
        print("=================MENU=================")
        print("0 - zakończ program")
        print("1 - Pokaż co u znajomych")
        print("2 - Dodaj nowego znajomego")
        print("3 - Usuń znajomego")
        print("======================================")
        choice = input("wybierz opcje menu: ")
        if choice == "0": break
        if choice == "1": get_user_info(users)
        if choice == "2": add_user(users)
        if choice == "3": remove_user(users)



if users == "main":
    main()
