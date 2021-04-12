from flask import Blueprint, render_template, request, redirect, url_for
from flask_cors import cross_origin
from ..database import db
from ..repository import user_repository, role_repository

buyer_routs = Blueprint('buyer_routs', __name__)


@buyer_routs.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    try:
        json_body = request.json
        first_name = json_body['first_name']
        second_name = json_body['second_name']
        third_name = json_body['third_name']
        email = json_body['email']
        password = json_body['password']
        if user_repository.email_is_free(email):
            return {"Error": "Мыло занято, меняй"}
        user_repository.add_new(second_name, first_name, third_name, password, email, 2)
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
