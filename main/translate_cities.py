import json
import os.path

cities = """Warszawa
Puławy
Warszawa
Warszawa
Warszawa
Chmielnik
Stargard
Warszawa
Otwock
Ostrołęka
Pleszew
Warszawa
Warszawa
Kutno
Otwock
Garwolin
Łuków
Warszawa
Mińsk Mazowiecki
Mińsk Mazowiecki
Otwock
Łódź
Stargard
Białogard
Police
Cieszyn
Szczecin
Bielsko-Biała
Chrzanów
Wadowice
Wadowice
Włodawa
Andrychów
Wadowice
Tarnobrzeg
Andrychów
Wadowice
Oświęcim
Wadowice
Kraków
Wadowice
Wadowice
Gorzeń Dolny
Wadowice
Przasnysz
Oświęcim
Andrychów
Wadowice
Wadowice
Wadowice
Wadowice
Andrychów
Wadowice
Wadowice
Andrychów
Myślenice
Bytom
Białogard
Police
Cieszyn
Szczecin
Białystok
Warszawa
Sandomierz
Radzyń Podlaski
Warszawa
Wołomin
Kraków
Maków Mazowiecki
Sokołów Podlaski
Ełk
Ostrołęka
Skarzysko Kamienna
Kozienice
Warszawa
Warszawa
Wołomin
Warszawa
Garwolin
Wysokie Mazowieckie
Płock
Warszawa
Nowy Dwór Mazowiecki
Końskie
Kutno
Ryki
Warszawa
Warszawa
Łuków
Wieluń
Nowy Dwór Mazowiecki
Wołomin
Warszawa
Glowno
Wyszków
Włodawa
Tarnobrzeg
Wadowice
Andrychów
Bytom
Wadowice
Gorzeń Dolny
Wadowice
Wadowice
Wadowice
Wadowice
Wadowice
Wadowice
Oświęcim
Kraków
Oświęcim
Wadowice
Bielsko-Biała
Wadowice
Chrzanów
Wadowice
Włodawa
Tarnobrzeg
Wadowice
Wadowice
Wadowice
Wadowice
Oświęcim
Wadowice
Wadowice
Andrychów
Kraków
Przasnysz
Myślenice
Kraków
Oświęcim
Kędzierzyn-Koźle
Kraków
Zamość
Przysietnica
Kraków
Bydgoszcz
Tczew
Żarki
Zabrze
Kraków
Kraków
Jasło
Pińczów
Dębica
Kalisz
Ostrowiec Swietokrzyski
Tomaszów Lubelski
Hrubieszów
Wadowice
Bielsko-Biała
Wadowice
Bytom
Wadowice
Tarnobrzeg
Andrychów
Wadowice
Wadowice
Wadowice
Myślenice
Wadowice
Wadowice
Wadowice
Andrychów
Wadowice
Gorzeń Dolny
Kraków
Andrychów
Wadowice
Włodawa
Andrychów
Oświecim
Oświęcim
Wadowice"""

with open(os.path.join(os.path.dirname(__file__), 'files', 'cities_locatives.json'), 'r') as cities_translator:
    data_json = json.load(cities_translator)


for city in cities.splitlines(keepends=False):
    data = data_json.get(city, '')
    print(data)

