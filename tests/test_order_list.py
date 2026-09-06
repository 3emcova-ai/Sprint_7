import requests
import allure

from data import Urls


class TestOrderList:

    @allure.title("Получение списка заказов, доступных для взятия курьером")
    def test_orders_get_list(self):
        payload = {'limit': '10', 'page': '0'}
        response_order_list = requests.get(f'{Urls.SCOOTER_URL}{Urls.CREATE_GET_ORDER}', params=payload)
        assert response_order_list.status_code == 200
        orders = response_order_list.json()['orders']
        assert isinstance(orders, list)
        assert len(orders) > 0
