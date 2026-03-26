import pytest
import requests
import allure
from utils.client import send_request, base_url
from src.Pet.pets import post_payload_required_with_param

# В этом тесте проверяется что данные котрые мы передали при создании записи сохранились корректно.
def test_get_pets_by_id(get_pet_id):

    with allure.step("Запрашиваем данные по заранее подготовленному Id"):
        pet_id = get_pet_id
        url = f"{base_url}/pet/{pet_id}"
        response = send_request(url=url, method="GET")
        assert response.status_code == 200

    with allure.step("Проверяем что id  в ответе совпадают с исходным"):
        assert pet_id == response.json()['id']

    with allure.step("Проверяем что name совпадает с исходным"):
        assert post_payload_required_with_param['name'] == response.json()['name']

    with allure.step("Проверяем что данные ссылки совпадают"):
        assert post_payload_required_with_param['photoUrls'] == response.json()['photoUrls']

