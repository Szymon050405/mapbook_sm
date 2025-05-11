users:list = [
    {"name":"Zuzia","location":"Radzyń_Podlaski","posts":700},

]
print(users)

def remove_user(users_data: list)->None:

    user_name=input("podaj imię użytkownika do usuniecia: ")
    for user in users_data:
        if user["name"] == user_name:
            users_data.remove(user)

remove_user(users)




print(users)