import requests
import pytest


URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b3672d5e94f54d1438e3896fee6519f3"
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = 36811


def test_status_code():                         # Проверка, что ответ запрос GET /trainers приходит с кодом 200
    response = requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response.status_code == 200     # утверждаю[assert], что статус-код запроса = 200


def test_response_contains_name():       # Проверка, что в ответе GET /trainers приходит строчка с именем твоего тренера
    response_get = requests.get(url=f'{URL}/trainers', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'shpilllka'
