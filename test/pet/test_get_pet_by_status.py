import requests
import allure
import pytest
from utils.client import base_url, send_request

@pytest.mark.parametrize("status", ['available', 'pending', 'sold'])
def test_get_pets(status):
    with allure.step(f"Проверяем что получаем код 200 при запросе данных о животных по статусу == {status}"):
        url = f"{base_url}/pet/findByStatus"
        response = send_request(url=url, method="GET", params={"status": status})
        assert response.status_code == 200
