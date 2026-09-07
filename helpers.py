import requests

from data import Urls


def courier_creation(generate_courier_data):
    return requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json=generate_courier_data)

def courier_login(login, password):
    return requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
    'login': login,
    'password': password
    })

def courier_get_id(login, password):
    response_courier_id = courier_login(login, password)
    return response_courier_id.json()['id']

def courier_delete(courier_id):
    return requests.delete(f'{Urls.SCOOTER_URL}{Urls.DELETE_COURIER}/{courier_id}')
    