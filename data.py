class Urls:
   SCOOTER_URL = "http://qa-scooter.praktikum-services.ru"
   CREATE_COURIER = "/api/v1/courier"
   LOGIN_COURIER = "/api/v1/courier/login"
   DELETE_COURIER = "/api/v1/courier"

class ResponseMessages:
    ERROR_WITHOUT_LOGIN_PASSWORD = 'Недостаточно данных для создания учетной записи'
    DUPLICATE_LOGIN = 'Этот логин уже используется'