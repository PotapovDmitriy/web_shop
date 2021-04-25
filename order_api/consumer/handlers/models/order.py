from order_api.backend_order.application.database import db


class Order(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, owner_id):
        self.owner_id = owner_id

    def to_json(self):
        return {
            "order_id": self.id,
            "owner_id": self.owner_id
        }
