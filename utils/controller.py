def get_user_info(users_data:list)->None:

    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowości{user["location"]} opublikował {user['posts']} postów")




def add_users(users_data: list)->None:

    users_name=input("podaj imię nowego użytkownika ")
    users_location=input("podaj lokalizacje nowego znajomego ")
    users_posts=int(input("podaj liczbe postów: "))
    users_data.append( {"name":users_name,"location":users_location,"posts":users_posts})

def remove_user(users_data: list)->None:

    user_name=input("podaj imię użytkownika do usuniecia: ")
    for user in users_data:
        if user["name"] == user_name:
            users_data.remove(user)