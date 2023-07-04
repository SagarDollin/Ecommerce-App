import requests
import json

def get_user(token):
    url_post = "http://127.0.0.1:8004/users/me/"
    user = requests.get(url_post, headers={'Authorization':f'Bearer {token}'})
    print(user)
    print(user.json())
    return user.json()

def get_token(username, password):
    url = "http://127.0.0.1:8004/token"

    payload= f'grant_type=&username={username}&password={password}&scope=&client_id=&client_secret='
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
    }
    token = requests.post(url, headers=headers, data=payload)
    print(token.text)
    return token.json()["access_token"]

def get_balance(token, username):
    url = f"http://127.0.0.1:8004/balance/?username={username}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 202:
        return response.json()
    else:
        return f"Request failed with status code {response.status_code}"
    
def signup(user):
    
    url = 'http://127.0.0.1:8004/users/signup/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "disabled": False,
        "password": user["password"]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.json()

def add_money(token, username, amount):
    url = 'http://127.0.0.1:8004/add/'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    params = {
        'add': amount,
        'username': username
    }
    response = requests.post(url, headers=headers, params=params)
    return response.json()



    

