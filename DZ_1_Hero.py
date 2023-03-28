from pprint import pprint
import requests
names_of_characters = ['Hulk', 'Captain America', 'Thanos']

#Заносим в переменную 'f' данные по всем героям из полученного по GET-запросу файла json
def super_heroes():
    url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(f'{url}/all.json')
    f = response.json()
    # pprint(f)
    # print(type(f))
    return f

#определяем самого умного героя
def heroes_name():
    hero_dict = {}
    for hero in super_heroes():
        if hero['name'] in names_of_characters:
            hero_dict[hero['name']] = hero['powerstats']['intelligence']
    max_intelligence = max(hero_dict.values())
    for key, value in hero_dict.items():
        if value == max_intelligence:
            print(f'{key} - самый умный: интелект = {max_intelligence}')
    print(hero_dict)

if __name__ == '__main__':
    super_heroes()
    heroes_name()
