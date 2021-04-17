from flask import Blueprint, request
from flask_cors import cross_origin
import requests
import json
from ..repository import cart_repository

category_routs = Blueprint('category_routs', __name__)


@category_routs.route('/new_cart', methods=['GET'])
@cross_origin(supports_credentials=True)
def create_new_cart():
    try:
        user_id = int(request.args.get("user_id"))
        cart = {"user_id": user_id,
                "products": None}
        cart_repository.cart_create(cart)
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/cart', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_cart():
    try:
        user_id = int(request.args.get("user_id"))
        cart_json = cart_repository.get_cart_by_user_id(user_id)
        return cart_json if cart_json else {"msg": "Empty"}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/add_product', methods=['GET'])
@cross_origin(supports_credentials=True)
def add_product():
    try:
        user_id = int(request.args.get("user_id"))
        product_id = int(request.args.get("product_id"))
        answer = requests.get("http://admin_api:5000/product?id=" + str(product_id))
        cart_repository.add_child(user_id, json.loads(answer.text))
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/delete_product', methods=['GET'])
@cross_origin(supports_credentials=True)
def delete_product_from_cart():
    try:
        user_id = int(request.args.get("user_id"))
        product_id = int(request.args.get("product_id"))
        return {"msg": cart_repository.delete_product(user_id, product_id)}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
