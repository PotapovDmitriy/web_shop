from ..repository import user_repository, role_repository


def authenticate(username, password):
    user = user_repository.get_by_login(username)
    if user and user.check_password(password):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_repository.get_by_id(user_id)
