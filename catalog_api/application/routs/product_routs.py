from flask import Blueprint, request
from ..repository import product_repository

product_routs = Blueprint('product_routs', __name__)


@product_routs.route('/', methods=['GET'])
def index():
    try:

        return "Index"
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@product_routs.route('/new_product', methods=['POST'])
def add_new_product():
    try:
        json_body = request.json
        print(str(json_body))
        # product_repository.product_create(json_body)
        return str(True)

    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)

