import pytest
import requests
import random
from src.Pet.pets import pet_id, Pets, post_payload_required_with_param
from utils.client import base_url, send_request
from src.Pet.pydantic_shemas.pet_put_schema import Pet_full_schema

@pytest.fixture()
def get_pet_id():
    url = f"{base_url}/pet"
    response = send_request(url=url,
                              method="Post",
                              headers={"Content-Type": "application/json"},
                              json=post_payload_required_with_param)
    pet_id = response.json()['id']
    return pet_id

@pytest.fixture()
def get_random_pet_data():

    url = f"{base_url}/pet/findByStatus"
    response = send_request(url=url, method="GET", params={"status": 'available'})
    pets_list = response.json()
    not_valide = True
    while not_valide:
        pet = random.choice(pets_list)
        try:
            if 'category' not in pet:
                continue
        except Exception as e:
            continue
        else:
            not_valide = False

    Pets.validate_schema_for_put_send(pet, Pet_full_schema)
    return pet
