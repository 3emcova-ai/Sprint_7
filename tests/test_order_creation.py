import pytest
import requests
import generators
import allure

from data import Urls


class TestOrderCreation:

    @allure.title("Создание заказа самоката цветом: BLACK, GREY, BLACK и GREY, без цвета")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_order_create_different_scooter_colors(self, colors):
        order_data = {
            'firstName': generators.firstname_generator(),
            'lastname': generators.lastname_generator(),
            'address': generators.address_generator(),
            'metro_station': generators.metro_station_generator(),
            'phone': generators.phone_generator(),
            'rent_time': generators.rent_time_generator(),
            'delivery_date': generators.delivery_date_generator(),
            'comment': generators.comment_generator(),
            "color": colors
        }
        response_order_different_colors = requests.post(f'{Urls.SCOOTER_URL}{Urls.CREATE_GET_ORDER}', json=order_data)
        assert response_order_different_colors.status_code == 201
        assert response_order_different_colors.json()['track'] > 0