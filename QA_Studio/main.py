import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b3672d5e94f54d1438e3896fee6519f3"
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}


# ----------------------------------------------------------------------------------------------------------
# 1. Создание покемона [POST /pokemons]

# create_pokemon_body = {
#     "name": "Peach",
#     "photo_id": 1004
# }
#
# response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=create_pokemon_body)
# print(response.text)

# ----------------------------------------------------------------------------------------------------------
# Отправить своего покемона в нокаут [POST /pokemons/knockout]
'''
knockout_body = {
    "pokemon_id": "342117"
}

response = requests.post(url=f'{URL}/pokemons/knockout', headers=HEADER, json=knockout_body)
print(response.text)
'''
# ----------------------------------------------------------------------------------------------------------
# Смена имени покемона [PATCH /pokemons]

# name_change_body = {
#     "pokemon_id": "358967",
#     "name": "New Name"
# }
#
# response = requests.patch(url=f'{URL}/pokemons', headers=HEADER, json=name_change_body)
# print(response.text)

# ----------------------------------------------------------------------------------------------------------
# Поймать покемона в покебол [POST /trainers/add_pokeball]

catch_pokemon_body = {
    "pokemon_id": "358967"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=catch_pokemon_body)
print(response.text)
