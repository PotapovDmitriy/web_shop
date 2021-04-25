from flask import Blueprint, request
from flask_cors import cross_origin
import requests
import json
from ..repository import *

cart_routs = Blueprint('cart_routs', __name__)


@cart_routs.route('/new_order', methods=['GET'])
@cross_origin(supports_credentials=True)
def create_new_order():
    try:
        user_id = int(request.args.get("user_id"))
        cart = {"user_id": user_id,
                "products": []}
        cart_repository.cart_create(cart)
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@cart_routs.route('/cart', methods=['GET'])
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
