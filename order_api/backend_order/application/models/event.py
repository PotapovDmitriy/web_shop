from ..database import db


class Event(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    version = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.String(50), unique=False, nullable=False)

    def __init__(self, order_id, version, status):
        self.order_id = order_id
        self.version = version
        self.status = status

    def to_json(self):
        return {
            "order_id": self.order_id,
            "version": self.version,
            "status": self.status
        }
