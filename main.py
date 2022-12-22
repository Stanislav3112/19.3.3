
import requests
import json
from datetime import datetime, timezone
import random
import config

# базовый URL
base_url = 'https://petstore.swagger.io/v2'

# GET /user/login  Logs user into the system

username = config.username  # Задаём имя пользователя
password = config.password  # Задаём пароль

res = requests.get(f'{base_url}/user/login?login={username}&password={password}',
                   headers={'accept': 'application/json'})

print('GET /user/login  Logs user into the system')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json())
print('  Ответ сервера header:', res.headers, '\n')

# POST

body = json.dumps(config.created_user)

res = requests.post(f'{base_url}/user', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=body)

print('POST /user  Create user')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# PUT

username = config.created_user['username']
body = json.dumps(config.updated_user)

res = requests.put(f'{base_url}/user/{username}',
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=body)

print('PUT /user/{username} Updated user')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# GET

username = config.updated_user['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print('GET /user/{username} Get user by user name (before delete)')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# DELETE

username = config.updated_user['username']

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print('DELETE /user/{username} Delete user')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# GET

username = config.updated_user['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print('GET /user/{username} Get user by user name (after delete) expected code 404')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# POST /user/createWithList Creates list of users with given input array

body = json.dumps(config.list_of_users)

res = requests.post(f'{base_url}/user/createWithList', headers={'accept': 'application/json',
                                                                'Content-Type': 'application/json'}, data=body)

print('POST /user/createWithList Creates list of users with given input array')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


print('POST /user/createWithArray Creates list of users with given input array')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# GET /user/logout  Logs out current logged in user session

res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})

print('GET /user/logout  Logs out current logged in user session')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


