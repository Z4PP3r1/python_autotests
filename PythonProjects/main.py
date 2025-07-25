import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'de58cfe2040e29ba21b433ab33cda175'
TRAINER_ID = '34226'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : f'{TOKEN}'}


create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

change_pokemon = {
    "pokemon_id": "363327",
    "name": "generate",
    "photo_id": -1
}

catch_pokemon = {
    "pokemon_id": "363327"
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADER,json=create_pokemon)
print(response.json())

response = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=change_pokemon)
print(response.json())

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER,json=catch_pokemon)
print(response.json())
