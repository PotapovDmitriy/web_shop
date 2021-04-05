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

    def to_json(self):
        return {
            "category_id": self.id,
            "name": self.name,
            "parent_name": self.get_parent().name if self.get_parent() is not None else None,
            "parent_category_id": self.parent_category_id,
            "isNil": self.nil
        }

    def get_children_if_exist(self):
        return db.session.query(Category).filter_by(parent_category_id=self.id).all()

    def count_of_children(self):
        if self.nil:
            return len(self.products)
        else:
            return len(self.get_children_if_exist())

    def get_parent(self):
        return db.session.query(Category).get(self.parent_category_id)

    def can_be_nil(self):
        return len(self.get_children_if_exist()) == 0
