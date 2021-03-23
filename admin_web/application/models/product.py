from ..database import db


class Product(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    summary = db.Column(db.String(800), unique=False, nullable=False)
    characteristic = db.Column(db.String(1000), unique=False, nullable=False)
    image_url = db.Column(db.String(1000), unique=False, nullable=False)

    # category = db.relationship('Category', backref='product')

    def __init__(self, name, category_id, price, summary, characteristic, url):
        self.name = name
        self.category_id = category_id
        self.price = price
        self.summary = summary
        self.characteristic = characteristic
        self.image_url = url
