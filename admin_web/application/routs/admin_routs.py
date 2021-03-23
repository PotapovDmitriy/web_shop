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


@admin_routs.route('/category', methods=['GET'])
def show_category():
    try:
        category = db.session.query(Category).get(1)
        if category is None:
            category = Category("Новая категория", None)
            db.session.add(category)
        product = db.session.query(Product).get(1)
        if product is None:
            product = Product("Продукт", 1, 12500, "summary", "characteristic")
            db.session.add(product)
        products = category.products

        db.session.commit()

        return str(category.products[0].name)
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
            return redirect(url_for("admin_routs.index"))
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
        form = request.form
        if request.method == "POST":
            name = request.form['name']
            category_id = None
            if request.form['category'] != "Не выбрана":
                category = db.session.query(Category).filter_by(name=request.form['category']).first()
                category_id = category.id
            price = request.form['price']
            summary = request.form['summary']
            characteristic = request.form['characteristic']

            files = request.files
            f = request.files['image']
            path = save_image(f, name)

            db.session.add(Product(name, category_id, price, summary, characteristic, path))
            db.session.commit()
            return redirect(url_for("admin_routs.index"))
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
