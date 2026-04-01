import requests
import pytest
import allure
import random
from utils.client import base_url, send_request, api_key
from src.Pet.pets import Pets

def test_delete_pet_from_store(get_random_pet_data):

    pet_id = get_random_pet_data['id']
    print(pet_id)
    url = f"{base_url}/pet/{pet_id}"

    with allure.step("Выполняем удаление товара по id"):
        response = send_request(url=url, method="DELETE", headers={"Content-Type": "application/json", 'api_key': api_key})

    with allure.step("Проверяем что вернулся код 200 по операции удаления"):
        assert response.status_code == 200

    with allure.step("Повторно выполняем поиск по id, чтобы проверить что товара нет в списке"):
        get_pet_by_id = requests.get(url=url)

    with allure.step("Проверяем что вернулся код ответа 404"):
        assert get_pet_by_id.status_code == 404

    with allure.step("проверяем что в ответе получено сообщение что товар не найден"):
        assert get_pet_by_id.json()['message'] == "Pet not found"