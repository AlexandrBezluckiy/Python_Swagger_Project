import requests


base_url = 'https://petstore.swagger.io/v2'
api_key = 'special-key'

def send_request(method, url, **kwargs):
    return requests.request(method, url, **kwargs)
