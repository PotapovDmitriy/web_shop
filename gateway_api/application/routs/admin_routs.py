from flask import Blueprint, render_template, request, redirect, url_for
import requests
from flask_cors import cross_origin
import json
from flask_jwt import JWT, jwt_required, current_identity

admin_routs = Blueprint('admin_routs', __name__)
ADMIN_API = "http://admin_api:5000/"


@admin_routs.before_request
@jwt_required()
def before_request():
    user = current_identity
    if user.role_id != 1:
        return {"msg": "you have no permission for this"}


@admin_routs.route('/new_category', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def create_category():
    try:
        json_body = request.json
        answer = requests.post(ADMIN_API + "new_category", json=json_body)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/categories', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_categories():
    try:
        answer = requests.get(ADMIN_API + "categories")
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/category', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_category():
    try:
        category_id = request.args.get("id")
        answer = requests.get(ADMIN_API + "category?id=" + str(category_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/delete_category', methods=['GET'])
@jwt_required()
@cross_origin(supports_credentials=True)
def delete_category():
    try:
        category_id = request.args.get("id")
        answer = requests.get(ADMIN_API + "delete_category?id=" + str(category_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/redact_category', methods=['POST'])
@jwt_required()
@cross_origin(supports_credentials=True)
def redact_category():
    try:
        json_body = request.json
        answer = requests.post(ADMIN_API + "redact_category", json=json_body)
        return str(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/new_product', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def create_product():
    try:
        json_body = request.json
        answer = requests.post(ADMIN_API + "new_product", json=json_body)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/products', methods=['GET'])
@cross_origin(supports_credentials=True)
def products():
    try:
        answer = requests.get(ADMIN_API + "products")
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/product', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_product():
    try:
        product_id = request.args.get("id")
        answer = requests.get(ADMIN_API + "product?id="+str(product_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/delete_product', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def delete_product():
    try:
        product_id = request.args.get("id")
        answer = requests.get(ADMIN_API + "delete_product?id=" + str(product_id))
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@admin_routs.route('/redact_product', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def redact_product():
    try:
        json_body = request.json
        answer = requests.post(ADMIN_API + "redact_product", json=json_body)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
