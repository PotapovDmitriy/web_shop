import bcrypt

from ..database import db
import datetime


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), unique=False, nullable=False)
    first_name = db.Column(db.String(200), unique=False, nullable=False)
    second_name = db.Column(db.String(250), unique=False, nullable=False)
    third_name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(300), unique=True, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __init__(self, second_name, first_name, third_name, password, email, role_id):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name
        self.email = email
        self.role_id = role_id
        self.set_hash_ps(password)

    def set_hash_ps(self, password):
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def get_full_name(self):
        return str(self.second_name) + " " + str(self.first_name) + " " + str(self.third_name)

    def get_student_json(self):
        return {"user_id": self.id,
                "first_name": self.first_name,
                "second_name": self.second_name,
                "third_name": self.third_name,
                "email": self.email,
                "login": self.login}

    def check_password(self, password):
        user_pass = str(self.password)
        return bcrypt.checkpw(password.encode('utf8'), user_pass.encode('utf-8'))
