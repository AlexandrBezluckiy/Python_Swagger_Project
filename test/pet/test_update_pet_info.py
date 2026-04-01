import requests
import pytest
import allure
import random
from utils.client import base_url, send_request
from src.Pet.pets import Pets

def test_update_pet_info(get_random_pet_data):


    with allure.step("С помощью фикстуры получаем даннае по записи"):
        pets_id = get_random_pet_data['id']

    url = f"{base_url}/pet/{pets_id}"

    with allure.step("Изменяем данные для отправки"):
        title = random.choice(['prince', 'lord', 'ser'])
        pets_new_name = f"{title}_{get_random_pet_data['name']}"
        pets_new_status = random.choice(['pending', 'sold', 'available'])

    with allure.step("Размещаем новые данные по сохраненному id"):
        send_new_pet_data = send_request(url=url, method="Post", headers={"Content-Type": "application/x-www-form-urlencoded"}, params={'name': str(pets_new_name), 'status': str(pets_new_status)})

    with allure.step("проверяем что код ответа 200"):
        assert send_new_pet_data.status_code == 200

    with allure.step("Запрашиваем данные по ранее сохраненному id."):
        get_pets = requests.get(url=url, params={'id': pets_id})
        assert get_pets.status_code == 200

    with allure.step("Проверяем что json в ответе не пустой."):
        assert len(get_pets.json()) > 0

    with allure.step("проверяем что вернулся ответ с верным id"):
        assert get_pets.json()['id'] == pets_id

    with allure.step("Проверяем что статус соответсвует переданному ранее статусу"):
        assert get_pets.json()['status'] == pets_new_status

    with allure.step("Проверяем что name соответствует ранее переданному статусу"):
        assert get_pets.json()['name'] == pets_new_name


