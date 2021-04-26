from ..database import db
import json

class Snapshot(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'snapshot'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    version = db.Column(db.Integer, unique=False, nullable=False)
    data = db.Column(db.Text(10000), unique=False, nullable=True)

    def __init__(self, order_id, version, data):
        self.order_id = order_id
        self.version = version
        self.data = data

    def to_json(self):
        data = json.loads(str(self.data).replace("\'", "\""))
        status = data['status']
        products = data['products']
        return {
            "order_id": self.order_id,
            "version": self.version,
            "products": products,
            "status" : status
        }
