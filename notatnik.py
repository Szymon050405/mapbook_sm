class User:
    def __init__(self, name, surname, location, posts):
        self.name = name
        self.surname = surname
        self.location = location
        self.posts = posts
        self.coordinates = self.get_coordinates()

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        try:
            latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
            longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
            print(latitude)
            print(longitude)
            return [latitude, longitude]
        except (IndexError, ValueError):
            print("Nie udało się pobrać współrzędnych.")
            return [0.0, 0.0]

# Tworzenie użytkownika
user_1 = User(name="Krzysztof", surname="Kowalski", location="Warszawa", posts=5)

# Wyświetlenie współrzędnych
print(user_1.coordinates)