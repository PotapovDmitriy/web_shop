from ..database import db
from ..models.event import Event


def add_new(order_id, version, status):
    event = Event(order_id, version, status)
    db.session.add(event)
    db.session.flush()
    db.session.refresh(event)
    db.session.commit()
    return event


def get_by_id(event_id):
    return db.session.query(Event).get(event_id)


def get_by_order(order_id) -> []:
    return db.session.query(Event).filter_by(order_id=order_id).all()


def get_all():
    return db.session.query(Event).all()


def delete(event) -> bool:
    db.session.delete(event)
    db.session.commit()
    return True
