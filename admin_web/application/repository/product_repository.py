from ..database import db
from ..models.product import Product


def add_new(name, category_id, price, summary, characteristic, path):
    product = Product(name, category_id, price, summary, characteristic, path)
    db.session.add(product)
    db.session.flush()
    db.session.refresh(product)
    db.session.commit()
    return product


def update(product, name, category_id, price, summary, characteristic, path):
    product.name = name
    product.category_id = category_id
    product.price = price
    product.summary = summary
    product.characteristic = characteristic
    product.path = path
    db.session.add(product)
    db.session.commit()
    return True


def get_by_id(product_id):
    return db.session.query(Product).get(product_id)


def get_by_name(product_name):
    return db.session.query(Product).filter_by(name=product_name).first()


def get_all():
    return db.session.query(Product).all()


def delete(product):
    db.session.delete(product)
    db.session.commit()
    return True
