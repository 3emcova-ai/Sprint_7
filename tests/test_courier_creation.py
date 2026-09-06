import requests
import generators
import allure

from data import Urls, ResponseMessages


class TestCourierCreation:

    @allure.title("Курьер успешно создан при передаче в ручку всех обязательных полей")
    def test_courier_created_successfully(self, generate_courier_with_deletion):
        _, _, _, courier_id = generate_courier_with_deletion
        assert courier_id > 0

    @allure.title("Код ответа - 201, при успешном создании курьера")
    def test_courier_created_response_code(self, generate_courier_with_deletion):
        _, response_create, _, _ = generate_courier_with_deletion
        assert response_create.status_code == 201
                
    @allure.title("Тело ответа - 'ok':true, при успешном создании курьера")
    def test_courier_created_response_text(self, generate_courier_with_deletion):
        _, response_create, _, _ = generate_courier_with_deletion
        assert response_create.json()['ok'] is True

    @allure.title("Ошибка при создании курьера при незаполненном поле login")
    def test_create_courier_withot_login_shows_error(self):
        response_without_login = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json={
        'login': "",
        'password': generators.password_generator(),
        'firstName': generators.firstname_generator()
    })
        assert response_without_login.status_code == 400
        assert response_without_login.json()['message'] == ResponseMessages.ERROR_CREATE_WITHOUT_LOGIN_PASSWORD

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_identical_couriers_cant_create(self, generate_courier_with_deletion):
        courier_data, _, _, _ = generate_courier_with_deletion
        response_repeat = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json=courier_data)
        assert response_repeat.status_code != 201

    @allure.title("Ошибка при создании пользователя с логином, который уже есть")
    def test_create_courier_when_login_repeat_shows_error(self, generate_courier_with_deletion):
        courier_data, _, _, _ = generate_courier_with_deletion
        response_repeat_login = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_COURIER}', json={
            'login': courier_data['login'],
            'password': generators.password_generator()
            })
        assert response_repeat_login.status_code == 409
        assert response_repeat_login.json()['message'] == ResponseMessages.DUPLICATE_LOGIN
