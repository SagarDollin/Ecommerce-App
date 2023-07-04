import requests

def get_brands(token):
    url = 'http://127.0.0.1:8004/categories/'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = ''
    response = requests.post(url, headers=headers)
    return response.json()

def search(token, search_key='', brand='Adidas', min_price=0, max_price=500):
    import requests

    url = 'http://127.0.0.1:8004/search/'
    params = {
        'search_key': search_key,
        'min_price': min_price,
        'max_price': max_price,
        'brand': brand
    }
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = ''

    response = requests.post(url, params=params, headers=headers, data=data)

    return response.json()