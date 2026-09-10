import pytest

from helpers import generate_courier_data, courier_delete, courier_creation_and_return_login_password


@pytest.fixture
def delete_courier_after_test():
    courier_ids = []
    yield courier_ids
    for courier_id in courier_ids:
        if courier_id:
            courier_delete(courier_id)

@pytest.fixture
def create_courier_and_registration():
    courier_data = generate_courier_data()
    new_courier = courier_creation_and_return_login_password(courier_data)
    assert new_courier is not None
    return courier_data
