import allure
import pytest
from src.Pet.pets import *
from utils.client import send_request, base_url
from src.Pet.pydantic_shemas.pet_post_shemas import Pet_Post

url = f"{base_url}/pet"

@pytest.mark.parametrize("json, expected_code",
                         [
                            (post_payload_without_name, 200),
                            (post_payload_without_url, 200),
                            (post_payload_required_with_param, 200),
                            (post_payload_full_param, 200)
                         ])
# Демо api не валидирует данные на входе, поэтому код 405 для двух последних случаев получить нельзя.
def test_create_new_pet(json, expected_code):
    with allure.step(f"Проверяем обязательность заполнения тегов {json}"):
        pet_response = Pets(send_request(url=url,
                                         method="POST",
                                         headers={"Content-Type": "application/json"},
                                         json=json))
        assert pet_response.response_code == expected_code


    with allure.step("Валидируем схему ответа от сервера при выполнении POST."):
        pet_response.validate_schema_for_post_response(Pet_Post)


