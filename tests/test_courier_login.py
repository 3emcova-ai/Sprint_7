import requests
import generators
import allure

from data import Urls, ResponseMessages


class TestCourierLogin:

    @allure.title("Курьер успешно авторизован при передаче в ручку всех обязательных полей")
    def test_courier_login_successfully(self, generate_courier_with_deletion):
        _, _, response_login, _ = generate_courier_with_deletion
        assert response_login.status_code == 200

    @allure.title("Получен id при успешной авторизации курьера")
    def test_courier_login_get_id(self, generate_courier_with_deletion):
        _, _, response_login, _ = generate_courier_with_deletion
        assert response_login.json()['id'] > 0

    @allure.title("Ошибка авторизации курьера при незаполненном поле password")
    def test_courier_login_withot_password_shows_error(self, generate_courier_with_deletion):
        courier_data, _, _, _ = generate_courier_with_deletion
        response_login_without_password = requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
            'login': courier_data['login'],
            'password': ""
            })
        assert response_login_without_password.status_code == 400
        assert response_login_without_password.json()['message'] == ResponseMessages.ERROR_LOGIN_WITHOUT_LOGIN_PASSWORD

    @allure.title("Ошибка авторизации курьера при указании неверного пароля")
    def test_courier_login_with_invalid_password_shows_error(self, generate_courier_with_deletion):
        courier_data, _, _, _ = generate_courier_with_deletion
        response_login_with_invalid_password = requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
            'login': courier_data['login'],
            'password': generators.password_generator()
            })
        assert response_login_with_invalid_password.status_code == 404
        assert response_login_with_invalid_password.json()['message'] == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND

    @allure.title("Ошибка авторизации несуществующего курьера")
    def test_non_existent_courier_login_shows_error(self):
        response_login_with_non_existent_courier = requests.post(f'{Urls.SCOOTER_URL}{Urls.LOGIN_COURIER}', json={
            'login': generators.login_generator(),
            'password': generators.password_generator()
            })
        assert response_login_with_non_existent_courier.status_code == 404
        assert response_login_with_non_existent_courier.json()['message'] == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND
        