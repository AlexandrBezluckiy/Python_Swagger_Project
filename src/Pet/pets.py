post_payload_full_param = {
    "id": 10001,
    "category": {
        "id": 101,
        "name": "Cats"
    },
    "name": "Murka",
    "photoUrls": ["https://img.freepik.com/free-photo/cute-kitten-sitting-looking-camera-fluffy-fur-playful-nature-generated-by-artificial-intelligence_188544-128186.jpg?semt=ais_hybrid"],

    "tags": [{
        "id": 201,
        "name": "rus_dvorovie"
    }],
    "status": "available"
}

post_payload_required_with_param = {
    "name" : "Vasilij",
    "photoUrls": ["https://img.freepik.com/free-photo/Jirnayz_jopa.jpg?semt=ais_hybrid"]
}

post_payload_without_name = {
    "photoUrls": ["https://img.freepik.com/free-photo/Jirnayz_jopa2.jpg?semt=ais_hybrid"]
}

post_payload_without_url = {
    "name" : "Vasilij"
}


pet_id = int()

class Pets:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_code = response.status_code


    def validate_schema_for_post_response(self, schema):
        schema(**self.response_json)

    @staticmethod
    def validate_schema_for_put_send(data, schema):
        schema(**data)
