import pytest
import generators
import requests
from data import Urls

@pytest.fixture
def generate_courier_with_deletion():

    courier_data = {
        'login': generators.login_generator(),
        'password': generators.password_generator(),
        'firstName': generators.firstname_generator()
    }
    response_create = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json=courier_data)
    
    courier_id = None
    response_login = None
    if response_create.status_code == 201:
        response_login = requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
            'login': courier_data['login'],
            'password': courier_data['password']
            })
        if response_login.status_code == 200:
            courier_id = response_login.json()['id']

    yield courier_data, response_create, response_login, courier_id
        
    if courier_id is not None:
        response_delete = requests.delete(f'{Urls.SCOOTER_URL}{Urls.DELETE_COURIER}/{courier_id}')
