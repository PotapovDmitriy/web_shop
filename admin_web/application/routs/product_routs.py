from flask import Blueprint, render_template, request, redirect, url_for

from ..database import db
from ..models.category import Category
from ..models.product import Product
from ..repository import product_repository, category_repository

product_routs = Blueprint('admin_routs', __name__)


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
def create_product():
    try:
        json_body = request.json
        name = json_body['name']

        category = category_repository.get_by_name(json_body["category"])
        category_id = category.id if category is not None else None
        price = json_body['price']
        summary = json_body['summary']
        characteristic = json_body['characteristic']
        path = json_body['image_url']

        product_repository.add_new(name, category_id, price, summary, characteristic, path)
        return {"msg": True}

    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@product_routs.route('/products', methods=['GET'])
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


@product_routs.route('/delete_product ', methods=['POST'])
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
def redact_product():
    try:
        json_body = request.json
        product_id = json_body.product_id
        product = db.session.query(Product).get(product_id)

        name = json_body['name']
        category = category_repository.get_by_name(json_body['category'])
        category_id = category.id if category is not None else None
        price = json_body['price']
        summary = json_body['summary']
        characteristic = json_body['characteristic']
        path = json_body['image_url']
        return {"msg": product_repository.update(product, name, category_id, price, summary, characteristic, path)}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
