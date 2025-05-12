users: list = [
    {"name":"Szymon","location":"Pruszków","posts":400},
    {"name":"Krzysztof","location":"Białobrzegi","posts":500},
    {"name":"Maja","location":"Świecie","posts":300},
    {"name":"Zuzanna","location":"Radzyń Podlaski","posts":700},
]

import folium





def get_coordinates(city_name:str)->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/{city_name}"
    response=requests.get(url).text
    response_html=BeautifulSoup(response,"html.parser")
    latitude=float(response_html.select(".latitude")[1].text.replace(",","."))
    longitude=float(response_html.select(".longitude")[1].text.replace(",","."))
    print(latitude)
    print(longitude)
    return [latitude,longitude]

for user in users:
    print(user["location"])
    get_coordinates(user["location"])

def get_map(users_data:list)->None:
    mapa = folium.Map(location=[52.333, 21.0], zoom_start=6)
    for user in users_data:
        print(user["location"])
        folium.Marker(location=get_coordinates(user["location"]),popup=f"{user["location"]} {user['name']}"
        ).add_to(mapa)
    mapa.save('mapa.html')

