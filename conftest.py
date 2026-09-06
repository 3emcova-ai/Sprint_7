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
    response = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json=courier_data)
    
    courier_id = None
    if response.status_code == 201:
        response_login = requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
            'login': courier_data['login'],
            'password': courier_data['password']
            })
        if response_login.status_code == 200:
            courier_id = response_login.json()['id']

    yield courier_data, response, courier_id
        
    if courier_id is not None:
        response_delete = requests.delete(f'{Urls.SCOOTER_URL}{Urls.DELETE_COURIER}/{courier_id}')

@pytest.fixture
def generate_courier_data_without_login():
    courier_data_without_login = {
        'password': generators.password_generator(),
        'firstName': generators.firstname_generator()
    }
    yield courier_data_without_login