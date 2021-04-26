from ..database import db
from ..models.snapshot import Snapshot


def add_new(order_id, version, data) -> None:
    snap = Snapshot(order_id, version, data)
    db.session.add(snap)
    db.session.commit()


def get_by_id(snap_id):
    return db.session.query(Snapshot).get(snap_id)


def update(snapshot, new_version, new_data):
    snapshot.version = new_version
    snapshot.data = new_data
    db.session.flush()
    db.session.refresh(snapshot)
    db.session.commit()
    return snapshot


def get_by_order(order_id) -> []:
    return db.session.query(Snapshot).filter_by(order_id=order_id).first()


def get_all():
    return db.session.query(Snapshot).all()


def delete(snap) -> bool:
    db.session.delete(snap)
    db.session.commit()
    return True
