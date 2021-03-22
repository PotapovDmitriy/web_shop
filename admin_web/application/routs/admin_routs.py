from flask import Blueprint

from ..database import db
from ..models.category import Category
from ..models.product import Product

admin_routs = Blueprint('admin_routs', __name__)


@admin_routs.route('/', methods=['GET'])
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
