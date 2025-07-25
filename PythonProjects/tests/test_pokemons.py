import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'de58cfe2040e29ba21b433ab33cda175'
TRAINER_ID = '34226'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : f'{TOKEN}'}

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url=f'{URL}/trainers',params={'trainer_id' : TRAINER_ID}, headers=HEADER)
    assert response.json()['data'][0]['trainer_name'] == 'Zapper'