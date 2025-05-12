users:list = [
    {"name":"Zuzia","location":"Radzyń_Podlaski","posts":700},

]
print(users)

def update_user(users_data: list)->None:

    user_name=input("podaj imię użytkownika którego dane chcesz zaktualizować: ")
    for user in users_data:
        if user["name"] == user_name:
            user["name"]= input("Podaj nowe imię użytkownika:")
            user["location"]= input("Podaj nową lokalizacje użytkownika:")
            user["location"]= int(input("Podaj nową liczbęm postów użytkownika:"))



update_user(users)




print(users)