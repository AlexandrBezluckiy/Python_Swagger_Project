import requests
import pytest
import allure
import copy
from utils.client import base_url, send_request
from src.Pet.pets import Pets

def test_put_random_pet(get_random_pet_data):
    url = f"{base_url}/pet"
    with allure.step("Получаем данные о новой записи json. Сохраняем id записи."):
        pet_data = get_random_pet_data
        pet_id = pet_data['id']
        # print('\nId записи: ', pet_id)

    with allure.step("Редактируем поля имя и название категории."):
        new_data_to_send = copy.deepcopy(pet_data)
        new_data_to_send['name'] = f"{new_data_to_send['name']}.auto"
        new_data_to_send['category']['name'] = 'autobots'

    with allure.step("Выполняем отправку скорректированного json на сервер."):
        updated_pets = send_request(url=url,
                                    method="PUT",
                                    headers={"Content-Type": "application/json"},
                                    json=new_data_to_send)

    with allure.step("Проверяем что вернулся статус 200"):
        assert updated_pets.status_code == 200