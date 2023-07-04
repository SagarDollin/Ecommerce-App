from fastapi import Depends, FastAPI
from Authentication.login import get_current_active_user, User
from server_app import app
from fastapi.security.api_key import APIKey

import pickle

from pymongo import MongoClient
from Authentication.login import *
# This is a file for product catalogue endpoints 

@app.post("/search/",status_code=202)
def search(search_key: str, min_price: float, max_price: float, brand: str, current_user: User = Depends(get_current_active_user)): # user needs to login to use this
    client = MongoClient('mongodb://localhost:27017/')
    with client:
        db = client.products_catalogue
        matched_products = db.products_info.find({ '$and': [{'price': {'$gt': min_price}}, {'price': {'$lt': max_price}}, {'name':{ '$regex' : search_key, '$options' : 'i' }}, {'brand': brand}]})
        print(matched_products)
        search_result_dict = dict()
        i = 1
        for prod in matched_products:
            try:
                del prod['_id']
            except:
                print("no id")
            search_result_dict[i] = prod
            i+=1

            # print(prod)
        print(search_result_dict)
        return search_result_dict
    

@app.post("/categories/",status_code=202)
def categories(current_user: User = Depends(get_current_active_user)):
    client = MongoClient('mongodb://localhost:27017/')
    with client:
        db = client.products_catalogue
        brands = db.products_info.distinct('brand')
    return {'brands': brands}

@app.post("/buy/",status_code=202)
def categories(id: str, current_user: User = Depends(get_current_active_user)):
    client = MongoClient('mongodb://localhost:27017/')
    with client:
        db = client.products_catalogue
        product_info = db.products_info.find_one({"id":id}) 
        print("product info", product_info)
        stock = product_info["stocks"]
        print("initial stock", stock)
        price = product_info["price"]
        myquery = { "id": id }
        newvalues = { "$set": { "stocks":  stock-1} }
        db.products_info.update_one(myquery, newvalues)
        product_info = db.products_info.find_one({"id":id}) 
        del product_info["_id"]
        return product_info


        






