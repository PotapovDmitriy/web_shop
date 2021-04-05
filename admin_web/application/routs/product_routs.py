from flask import Blueprint, render_template, request, redirect, url_for
from flask_cors import cross_origin
from ..database import db
from ..messages import message
from ..models.product import Product
from ..repository import product_repository

product_routs = Blueprint('product_routs', __name__)


@product_routs.route('/', methods=['GET'])
def index():
    try:
        db.create_all()
        return "Index"
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@product_routs.route('/new_product', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def create_product():
    try:
        json_body = request.json
        name = json_body['name']

        category_id = json_body["category_id"]
        price = json_body['price']
        summary = json_body['summary']
        characteristic = json_body['characteristic']
        path = json_body['image_url']

        new_product = product_repository.add_new(name, category_id, price, summary, characteristic, path)
        # message.send_message_for_create_product(new_product.to_json())
        return {"msg": True}

    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@product_routs.route('/products', methods=['GET'])
@cross_origin(supports_credentials=True)
def products():
    try:
        all_products = product_repository.get_all()
        products_json_arr = []
        for product in all_products:
            products_json_arr.append(product.to_json())
        return {"products": products_json_arr}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@product_routs.route('/product', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_product():
    try:
        product_id = request.args.get("id")
        product = product_repository.get_by_id(product_id)
        return product.to_json()
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@product_routs.route('/delete_product', methods=['GET'])
@cross_origin(supports_credentials=True)
def delete_product():
    try:
        product_id = request.args.get("id")
        product = product_repository.get_by_id(product_id)
        return {"msg":product_repository.delete(product)}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@product_routs.route('/redact_product', methods=['POST'])
@cross_origin(supports_credentials=True)
def redact_product():
    try:
        json_body = request.json
        product_id = request.args.get("id")
        product = db.session.query(Product).get(product_id)

        name = json_body['name']
        category_id = json_body['category_id']

        price = json_body['price']
        summary = json_body['summary']
        characteristic = json_body['characteristic']
        image_url = json_body['image_url']
        return {"msg": product_repository.update(product, name, category_id, price, summary, characteristic, image_url)}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
