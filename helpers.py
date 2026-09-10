import requests
import allure
import generators

from data import Urls

@allure.step('Гененирую Логин, Пароль и Имя для регистрации курьера')
def generate_courier_data():
    courier_data = {
        'login': generators.login_generator(),
        'password': generators.password_generator(),
        'firstName': generators.firstname_generator()
    }
    return courier_data

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

@allure.step('Регистрирую курьера и возвращаю список из логина и пароля')
def courier_creation_and_return_login_password(courier_data):
    response = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json=courier_data)
    if response.status_code == 201:
        return (courier_data['login'], courier_data['password'])
    return None 
