from ..database import db

class Role(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "ID" + self.id + "   Name " + self.name
