from utilis.model import users
from utilis.controller import get_user_info

def main():
    while True:
        print("=================MENU=================")
        print("0 - zakończ program")
        print("1 - Pokaż co u znajomych")
        print("======================================")
        choice = input("wybierz opcje menu: ")
        if choice == "0": break
        if choice == "1": get_user_info(users)


if users == "main":
    main()

