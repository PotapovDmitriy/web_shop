from ..database import db
from ..models.category import Category


def add_new(name, parent_id, is_nil):
    category = Category(name, parent_id, is_nil)
    db.session.add(category)
    db.session.flush()
    db.session.refresh(category)
    db.session.commit()
    return category


def update(category, new_name, new_parent_category, is_nil):
    category.name = new_name
    category.parent_category_id = new_parent_category
    category.nil = is_nil
    db.session.add(category)
    db.session.flush()
    db.session.refresh(category)
    db.session.commit()
    return category


def get_by_id(cat_id):
    return db.session.query(Category).get(cat_id)


def get_by_name(cat_name):
    return db.session.query(Category).filter_by(name=cat_name).first()


def get_all():
    return db.session.query(Category).all()


def delete(category):
    db.session.delete(category)
    db.session.commit()
    return True

