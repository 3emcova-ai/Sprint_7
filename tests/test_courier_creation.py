import generators
import allure

from data import ResponseMessages
from helpers import courier_creation, courier_login, courier_get_id


class TestCourierCreation:

    @allure.title("Курьер успешно создан при передаче в ручку всех обязательных полей")
    def test_courier_created_successfully(self, generate_courier_data, delete_courier_after_test):
        response_create = courier_creation(generate_courier_data)
        courier_id = courier_get_id(generate_courier_data['login'], generate_courier_data['password'])
        assert response_create.status_code == 201
        assert courier_id > 0
        delete_courier_after_test.append(courier_id)

    @allure.title("Код ответа - 201, при успешном создании курьера")
    def test_courier_created_response_code(self, generate_courier_data, delete_courier_after_test):
        response_create = courier_creation(generate_courier_data)
        assert response_create.status_code == 201
        courier_id = courier_get_id(generate_courier_data['login'], generate_courier_data['password'])
        delete_courier_after_test.append(courier_id)
                
    @allure.title("Тело ответа - 'ok':true, при успешном создании курьера")
    def test_courier_created_response_text(self, generate_courier_data, delete_courier_after_test):
        response_create = courier_creation(generate_courier_data)
        assert response_create.json()['ok'] is True
        courier_id = courier_get_id(generate_courier_data['login'], generate_courier_data['password'])
        delete_courier_after_test.append(courier_id)

    @allure.title("Ошибка при создании курьера при незаполненном поле login")
    def test_create_courier_withot_login_shows_error(self):
        courier_data_without_login = {
            'login': "",
            'password': generators.password_generator(),
            'firstName': generators.firstname_generator()
            }
        response_without_login = courier_creation(courier_data_without_login)
        assert response_without_login.status_code == 400
        assert response_without_login.json()['message'] == ResponseMessages.ERROR_CREATE_WITHOUT_LOGIN_PASSWORD

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_identical_couriers_cant_create(self, generate_courier_data, delete_courier_after_test):
        response_create = courier_creation(generate_courier_data)
        response_repeat_courier_data = courier_creation(generate_courier_data)
        assert response_repeat_courier_data.status_code == 409
        courier_id = courier_get_id(generate_courier_data['login'], generate_courier_data['password'])
        delete_courier_after_test.append(courier_id)

    @allure.title("Ошибка при создании пользователя с логином, который уже есть")
    def test_create_courier_when_login_repeat_shows_error(self, generate_courier_data, delete_courier_after_test):
        response_create = courier_creation(generate_courier_data)
        courier_data_login = {
            'login': generate_courier_data['login'],
            'password': generators.password_generator(),
            'firstName': generators.firstname_generator()
            }
        response_repeat_login = courier_creation(courier_data_login)
        assert response_repeat_login.status_code == 409
        assert response_repeat_login.json()['message'] == ResponseMessages.DUPLICATE_LOGIN
        courier_id = courier_get_id(generate_courier_data['login'], generate_courier_data['password'])
        delete_courier_after_test.append(courier_id)
