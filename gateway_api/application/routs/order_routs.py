from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt import JWT, jwt_required, current_identity
import requests
import json

order_routs = Blueprint('order_routs', __name__)

ORDER_API = "http://order_api:5018/"


@order_routs.route('/cancel_order', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def cancel_order():
    try:
        order_id = request.args.get("id")
        user = current_identity
        user_role = user.role_id
        json_data = {"role_id": user_role,
                     "order_id": order_id}
        answer = requests.post(ORDER_API + "cancel_order", json=json_data)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@order_routs.route('/confirm_order', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def confirm_order():
    try:
        order_id = request.args.get("id")
        user = current_identity
        user_role = user.role_id
        json_data = {"role_id": user_role,
                     "order_id": order_id}
        answer = requests.post(ORDER_API + "confirm_order", json=json_data)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@order_routs.route('/execute_order', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def execute_order():
    try:
        order_id = request.args.get("id")
        user = current_identity
        user_role = user.role_id
        json_data = {"role_id": user_role,
                     "order_id": order_id}
        answer = requests.post(ORDER_API + "execute_order", json=json_data)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@order_routs.route('/all_orders', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_all_orders():
    try:
        user = current_identity
        user_role = user.role_id
        user_id = user.id
        json_data = {"role_id": user_role,
                     "user_id": user_id}
        answer = requests.post(ORDER_API + "all_orders", json=json_data)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@order_routs.route('/get_order', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_order():
    try:
        order_id = request.args.get("id")
        answer = requests.get(ORDER_API + "get_order?id=" + order_id)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
