import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    'firstname': 'D1',
    'lastname': 'Jfggdn',
    'email': 'jgfn@ew.com',
    'nickname': 'ketld',
    'password': '1dfqfjv'
}

response = requests.post('http://127.0.0.1:8000/users/', headers=headers, json=json_data)

print(response.text)