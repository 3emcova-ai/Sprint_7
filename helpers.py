import requests
import allure

from data import Urls

@allure.step('Регистрирую курьера')
def courier_creation(courier_data):
    return requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json=courier_data)

@allure.step('Осуществляю авторизацию курьера')
def courier_login(login, password):
    return requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
    'login': login,
    'password': password
    })

@allure.step('Получаю id зарегистрированного курьера')
def courier_get_id(login, password):
    response_courier_id = courier_login(login, password)
    if response_courier_id.status_code == 200:
        return response_courier_id.json()['id']
    return None

@allure.step('Удаляю курьера')
def courier_delete(courier_id):
    return requests.delete(f'{Urls.SCOOTER_URL}{Urls.DELETE_COURIER}/{courier_id}')
    