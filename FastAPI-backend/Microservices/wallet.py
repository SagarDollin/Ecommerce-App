from fastapi import Depends, FastAPI
from Authentication.login import get_current_active_user, User
from server_app import app
from fastapi.security.api_key import APIKey

import pickle
from Authentication.login import *
from pymongo import MongoClient

@app.post("/spend/",status_code=202)
def spend(spent: float, username: str, current_user: User = Depends(get_current_active_user) ):
    client = MongoClient('mongodb://localhost:27017/')
    with client:
        db = client.users
        wallet_info = db.wallets_info.find_one({"username":username})
        if wallet_info:
            balance = wallet_info["balance"]
            if balance > spent:
                balance = balance-spent
                wallet_info["balance"] = balance
                myquery = { "username": username }
                newvalues = { "$set": { "balance":  balance} }
                db.wallets_info.update_one(myquery, newvalues)
                updated_wallet = db.wallets_info.find_one({'username': username})
                del updated_wallet['_id']
                return updated_wallet
            else:
                return "Insufficient Balance"
        else:
            return "User doesn't exists or doesn't have a wallet"

@app.post("/add/",status_code=202)
def add(add: float, username: str, current_user: User = Depends(get_current_active_user) ):
    client = MongoClient('mongodb://localhost:27017/')
    with client:
        db = client.users
        wallet_info = db.wallets_info.find_one({"username":username})
        if wallet_info:
            balance = wallet_info["balance"]
            balance = balance + add
            myquery = { "username": username }
            newvalues = { "$set": { "balance":  balance} }
            db.wallets_info.update_one(myquery, newvalues)
            updated_wallet = db.wallets_info.find_one({'username': username})
            del updated_wallet['_id']
            return updated_wallet
          
        else:
            return "User doesn't exists or doesn't have a wallet"

@app.get("/balance/", status_code=202)
def get_balance(username: str, current_user: User = Depends(get_current_active_user)):
    client = MongoClient('mongodb://localhost:27017/')
    with client:
        db = client.users
        wallet_info = db.wallets_info.find_one({"username":username})
        if wallet_info:
            balance = wallet_info["balance"] 
        else:
            balance = 500
            user = db.users_info.find_one({'username': username})
            if user:
                wallet_info = {
                    "username": username,
                    "balance": balance
                }
                db.wallets_info.insert_one(wallet_info)
                new_wallet_info = db.wallets_info.find_one({"username":username})
                balance = new_wallet_info["balance"]
            else:
                return "User doesn't Exists"
        return balance
