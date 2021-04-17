from flask import Blueprint, render_template, request, redirect, url_for
import requests
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import cross_origin
from flask_jwt import JWT, jwt_required, current_identity
from ..database import db
import json
from ..repository import user_repository, role_repository

buyer_routs = Blueprint('buyer_routs', __name__)
CATALOG_API = "http://catalog_api:5010/"


@buyer_routs.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    try:
        json_body = request.json
        first_name = json_body['first_name']
        second_name = json_body['second_name']
        third_name = json_body['third_name']
        login = json_body['login']
        password = json_body['password']
        if not user_repository.login_is_free(login):
            return {"Error": "Login занят, меняй"}
        user_repository.add_new(second_name, first_name, third_name, password, login, 2)
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@buyer_routs.route('/root_categories', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_root_categories():
    try:
        answer = requests.get(CATALOG_API + "root_categories")

        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@buyer_routs.route('/category', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_category():
    try:
        category_id = request.args.get("id")
        connection_str = CATALOG_API + "/category?id=" + str(category_id)
        answer = requests.get(connection_str)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
