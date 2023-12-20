import requests
from getpass import getpass


endpoint = 'http://127.0.0.1:8000/auth/'
username = input('enter your username: \n')
password = getpass('enter your password: \n')
auth_response = requests.post(endpoint, json={'username': username, 'password': password})
print(auth_response.json())
print(auth_response.status_code)

if auth_response.status_code == 200:
    endpoint = 'http://127.0.0.1:8000/api/list'
    headers = {
        'Authorization': 'Token c8cab7e1263beafd696fec3fbff93ebdb1eae9a6'
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)
