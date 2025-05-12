def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowości {user['location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    user_name = input("Podaj imię nowego użytkownika: ")
    user_location = input("Podaj lokalizacje nowego znajomego: ")
    user_posts = int(input("Podaj liczbę postów: "))
    users_data.append({"name": user_name, "location": user_location, "posts": user_posts})


def remove_user(users_data: list) -> None:
    user_name = input("Podaj imie użytkownika do usunięcia: ")
    for user in users_data:
        if user["name"] == user_name:
            users_data.remove(user)
