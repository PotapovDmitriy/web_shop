from flask import Blueprint, render_template, request, redirect, url_for
import requests
from flask_cors import cross_origin
from ..database import db
import json

buyer_routs = Blueprint('buyer_routs', __name__)
CATALOG_API = "http://catalog_api:5010/"


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


@buyer_routs.route('/category', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_category():
    try:
        category_id = request.args.get("id")
        connection_str = CATALOG_API + "category?id=" + str(category_id)
        answer = requests.get(connection_str)
        return json.loads(answer.text)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
