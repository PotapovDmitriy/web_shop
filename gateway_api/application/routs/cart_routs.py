from flask import Blueprint, request
from flask_cors import cross_origin
import requests
import json
from flask_jwt import JWT, jwt_required, current_identity

cart_routs = Blueprint('cart_routs', __name__)

CART_API = "http://cart_api:5015/"


@cart_routs.before_request
@jwt_required()
def before_request():
    user = current_identity
    if user.role_id != 2:
        return {"msg": "you have no permission for this"}


@cart_routs.route('/cart', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_cart():
    try:
        user = current_identity
        user_id = user.id
        answer = requests.get(CART_API + "cart?user_id=" + str(user_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@cart_routs.route('/add_product', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def add_product():
    try:
        user_id = current_identity.id
        product_id = int(request.args.get("product_id"))
        answer = requests.get(CART_API + "add_product?product_id=" + str(product_id) + "&user_id=" + str(user_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@cart_routs.route('/delete_product', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def delete_product_from_cart():
    try:
        user_id = current_identity.id
        product_id = int(request.args.get("product_id"))
        answer = requests.get(CART_API + "delete_product?product_id=" + str(product_id) + "&user_id=" + str(user_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@cart_routs.route('/product_minus_one', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def product_minus_one():
    try:
        user_id = current_identity.id
        product_id = int(request.args.get("product_id"))
        answer = requests.get(CART_API + "product_minus_one?product_id=" + str(product_id) + "&user_id=" + str(user_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@cart_routs.route('/new_order', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def create_order():
    try:
        user_id = current_identity.id
        answer = requests.get(CART_API + "order?user_id=" + str(user_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
