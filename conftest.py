import pytest
import generators

from helpers import courier_delete

@pytest.fixture
def generate_courier_data():
    courier_data = {
        'login': generators.login_generator(),
        'password': generators.password_generator(),
        'firstName': generators.firstname_generator()
    }
    yield courier_data

@pytest.fixture
def delete_courier_after_test():
    courier_ids = []
    yield courier_ids
    for courier_id in courier_ids:
        if courier_id:
            courier_delete(courier_id)
