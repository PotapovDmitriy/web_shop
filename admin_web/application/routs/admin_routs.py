from flask import Blueprint, render_template, request, redirect, url_for

from ..database import db
from ..models.category import Category
from ..models.product import Product
from ..repository import category_repository

admin_routs = Blueprint('admin_routs', __name__)


@admin_routs.route('/', methods=['GET'])
def index():
    try:
        db.create_all()
        return render_template('index.html')
    except Exception as ex:

        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@admin_routs.route('/new_product', methods=['GET', 'POST'])
def create_product():
    try:
        if request.method == "POST":
            name = request.form['name']
            category_id = None
            if request.form['category'] != "Не выбрана":
                category = db.session.query(Category).filter_by(name=request.form['category']).first()
                category_id = category.id
            price = request.form['price']
            summary = request.form['summary']
            characteristic = request.form['characteristic']

            # files = request.files
            # f = request.files['image']
            # path = save_image(f, name)
            path = request.form['image']

            db.session.add(Product(name, category_id, price, summary, characteristic, path))
            db.session.commit()
            return redirect(url_for("admin_routs.products"))
        if request.method == "GET":
            nil_categories = db.session.query(Category).filter_by(nil=True).all()
            return render_template('new_product.html', categories=nil_categories)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@admin_routs.route('/products', methods=['GET'])
def products():
    try:
        all_products = db.session.query(Product).all()
        return render_template('products.html', products=all_products)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@admin_routs.route('/delete_product ', methods=['POST'])
def delete_product():
    try:
        pr_id = request.form["id"]
        product = db.session.query(Product).get(pr_id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for("admin_routs.products"))
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@admin_routs.route('/product/<id>', methods=['GET', 'POST'])
def redact_product(id):
    try:

        product = db.session.query(Product).get(id)
        if request.method == "POST":
            name = request.form['name']
            category_id = None
            if request.form['category'] != "Не выбрана":
                category = db.session.query(Category).filter_by(name=request.form['category']).first()
                category_id = category.id
            price = request.form['price']
            summary = request.form['summary']
            characteristic = request.form['characteristic']

            # files = request.files
            # f = request.files['image']
            # path = save_image(f, name)
            path = request.form['image']

            product.name = name
            product.price = price
            product.characteristic = characteristic
            product.summary = summary
            product.image_url = path
            db.session.add(product)
            db.session.commit()
            return redirect(url_for("admin_routs.products"))
        if request.method == "GET":
            nil_categories = db.session.query(Category).filter_by(nil=True).all()
            return render_template('redact_product.html', categories=nil_categories, product=product)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
