import generators
import allure

from data import ResponseMessages
from helpers import courier_login, courier_get_id


class TestCourierLogin:

    @allure.title("Курьер успешно авторизован при передаче в ручку всех обязательных полей")
    def test_courier_login_successfully(self, create_courier_and_registration, delete_courier_after_test):
        response_login = courier_login(create_courier_and_registration['login'], create_courier_and_registration['password'])
        assert response_login.status_code == 200
        courier_id = courier_get_id(create_courier_and_registration['login'], create_courier_and_registration['password'])
        delete_courier_after_test.append(courier_id)

    @allure.title("Получен id при успешной авторизации курьера")
    def test_courier_login_get_id(self, create_courier_and_registration, delete_courier_after_test):
        response_login = courier_login(create_courier_and_registration['login'], create_courier_and_registration['password']) 
        assert response_login.json()['id'] > 0
        courier_id = courier_get_id(create_courier_and_registration['login'], create_courier_and_registration['password'])
        delete_courier_after_test.append(courier_id)

    @allure.title("Ошибка авторизации курьера при незаполненном поле password")
    def test_courier_login_withot_password_shows_error(self, create_courier_and_registration, delete_courier_after_test):
        response_login_without_password = courier_login(create_courier_and_registration['login'], "")
        assert response_login_without_password.status_code == 400
        assert response_login_without_password.json()['message'] == ResponseMessages.ERROR_LOGIN_WITHOUT_LOGIN_PASSWORD
        courier_id = courier_get_id(create_courier_and_registration['login'], create_courier_and_registration['password'])
        delete_courier_after_test.append(courier_id)

    @allure.title("Ошибка авторизации курьера при указании неверного пароля")
    def test_courier_login_with_invalid_password_shows_error(self, create_courier_and_registration, delete_courier_after_test):
        response_login_with_invalid_password = courier_login(create_courier_and_registration['login'], generators.password_generator())
        assert response_login_with_invalid_password.status_code == 404
        assert response_login_with_invalid_password.json()['message'] == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND
        courier_id = courier_get_id(create_courier_and_registration['login'], create_courier_and_registration['password'])
        delete_courier_after_test.append(courier_id)

    @allure.title("Ошибка авторизации несуществующего курьера")
    def test_non_existent_courier_login_shows_error(self):
        response_login_with_non_existent_courier = courier_login(generators.login_generator(), generators.password_generator())
        assert response_login_with_non_existent_courier.status_code == 404
        assert response_login_with_non_existent_courier.json()['message'] == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND
        