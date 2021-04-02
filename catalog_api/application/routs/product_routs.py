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
        product_repository.product_create(json_body)
        return str(True)

    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@product_routs.route('/products', methods=['GET'])
def products():
    try:
        category_id = request.args.get("category_id")
        all_products = product_repository.get_products_by_category_id(category_id)
        return {"products": all_products}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@product_routs.route('/product', methods=['GET'])
def get_product():
    try:
        product_id = request.args.get("id")
        product = product_repository.get_product_by_id(product_id)
        return product.to_json()
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@product_routs.route('/delete_product', methods=['GET'])
def delete_product():
    try:
        product_id = request.args.get("id")
        product_repository.product_delete(product_id)
        return {"msg":True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@product_routs.route('/redact_product', methods=['POST'])
def redact_product():
    try:
        json_body = request.json
        product_repository.product_update(json_body)
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)

