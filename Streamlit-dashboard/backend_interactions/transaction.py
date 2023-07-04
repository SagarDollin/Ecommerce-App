import requests

def transaction(username,product_id, token, amount):
    # Deduct Balance
    url = 'http://127.0.0.1:8004/spend/'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    params = {
        'spent': amount,
        'username': username
    }
    updated_wallet = requests.post(url, headers=headers, params=params)
    updated_wallet = updated_wallet.json()
    print(f"wallet: {updated_wallet}")
    if updated_wallet == "Insufficient Balance":
        return "Insufficient Balance"
    else:
        new_balance = updated_wallet["balance"]
        
        # Update Stocks
        url = 'http://127.0.0.1:8004/buy/'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        params = {
            'id': product_id
        }
        product = requests.post(url, headers=headers, params=params)
        product = product.json()
        try:
            
            stocks = product["stocks"]
        except Exception as e:
            print(e)
            return "Something went wrong, refer to logs!"
        return {"balance": new_balance, "stocks":stocks}

    



