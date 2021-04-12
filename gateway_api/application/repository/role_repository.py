from ..models.role import Role
from ..database import db


def add_new(name):
    new_role = Role(name)
    db.session.add(new_role)
    db.session.commit()
    return new_role


def update(role_id, new_name):
    role = get_by_id(role_id)
    role.name = new_name
    db.session.add(role)
    db.session.commit()
    return True


def get_by_id(role_id):
    return db.session.query(Role).get(role_id)


def get_by_name(name):
    return db.session.query(Role).filter_by(name=name).first()
