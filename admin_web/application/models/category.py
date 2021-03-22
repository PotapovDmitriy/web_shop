from ..database import db


class Category(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    parent_category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    nil = db.Column(db.Boolean, nullable=True)

    products = db.relationship('Product', backref='category')

    def __init__(self, name, parent_id, nil=False):
        self.name = name
        self.parent_category_id = parent_id
        self.nil = nil

    def __repr__(self):
        return '<Category: {}>'.format(self.id)
