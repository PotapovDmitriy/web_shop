from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt import JWT, jwt_required, current_identity
from ..repository import user_repository, role_repository
from ..database import db

auth_routs = Blueprint('auth_routs', __name__)


@auth_routs.route('/register', methods=['POST'])
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


@auth_routs.route('/user', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def get_cart():
    try:
        user = current_identity
        return user.to_json()
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
