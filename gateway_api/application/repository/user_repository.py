from ..models.user import User
from ..database import db


def add_new(second_name, first_name, third_name, password, email, role_id):
    new_user = User(second_name, first_name, third_name, password, email, role_id)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def check_existence(user_id):
    return get_by_id(user_id) is not None


def update(user_id, second_name, first_name, third_name, email):
    user = get_by_id(user_id)
    user.first_name = first_name
    user.second_name = second_name
    user.third_name = third_name
    user.email = email
    db.session.add(user)
    db.session.commit()
    return True


def update_passwd(user, new_password):
    user.set_hash_ps(new_password)
    user.set_date_of_change()
    db.session.add(user)
    db.session.commit()
    return True


def get_by_id(user_id):
    return db.session.query(User).get(user_id)


def get_by_email(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user


def email_is_free(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user is None


def delete(user):
    try:
        if user is None:
            return True
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception as ex:
        print("-------------------------")
        print("Exception:" + str(ex))
        print("-------------------------")
        return False


def get_all():
    return db.session.query(User).all()
