from flask import Blueprint, render_template, request, redirect, url_for

from ..database import db
from ..models.category import Category
from ..models.product import Product
from ..services.file_servise import save_image

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


@admin_routs.route('/new_category', methods=['GET', 'POST'])
def create_category():
    try:
        if request.method == "POST":
            form = request.form
            name = request.form['name']
            parent_id = None
            if request.form['parent'] != "Не выбрана":
                parent = db.session.query(Category).filter_by(name=request.form['parent']).first()
                parent_id = parent.id
            is_nil = False
            if "isNil" in dict(request.form):
                if request.form['isNil'] == "on":
                    is_nil = True

            db.session.add(Category(name, parent_id, is_nil))
            db.session.commit()
            return redirect(url_for("admin_routs.categories"))
        if request.method == "GET":
            parents_category = db.session.query(Category).filter_by(nil=False).all()
            return render_template('new_category.html', parents=parents_category)
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


@admin_routs.route('/categories ', methods=['GET'])
def categories():
    try:
        all_categories = db.session.query(Category).all()
        return render_template('categories.html', categories=all_categories)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@admin_routs.route('/delete_category ', methods=['POST'])
def delete_category():
    try:
        cat_id = request.form["id"]
        category = db.session.query(Category).get(cat_id)
        if len(category.products) != 0 or len(category.get_children_if_exist()) != 0:
            return "НЕльзя удалять категорию у которой есть дочки"
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for("admin_routs.categories"))
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


@admin_routs.route('/category/<id>', methods=['GET', 'POST'])
def redact_category(id):
    try:

        category = db.session.query(Category).get(id)
        if request.method == "POST":
            name = request.form['name']
            parent_id = None
            if request.form['parent'] != "Не выбрана":
                parent = db.session.query(Category).filter_by(name=request.form['parent']).first()
                parent_id = parent.id
            is_nil = False
            if "isNil" in dict(request.form):
                if request.form['isNil'] == "on":
                    is_nil = True
            category.name = name
            category.parent_category_id = parent_id
            category.nil = is_nil
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("admin_routs.categories"))
        if request.method == "GET":
            parents_category = db.session.query(Category).filter_by(nil=False).all()
            return render_template('redact_category.html', parents=parents_category, category=category)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
