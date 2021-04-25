from order_api.backend_order.application.database import db
from ..models.order import Order


def add_new(owner_id):
    order = Order(owner_id)
    db.session.add(order)
    db.session.flush()
    db.session.refresh(order)
    db.session.commit()
    return order


def get_by_id(order_id):
    return db.session.query(Order).get(order_id)


def get_by_owner(owner_id) -> []:
    return db.session.query(Order).filter_by(owner_id=owner_id).all()


def get_all():
    return db.session.query(Order).all()


def delete(order) -> bool:
    db.session.delete(order)
    db.session.commit()
    return True
