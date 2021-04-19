from application import create_app
from application.database import db
from application.repository import role_repository, user_repository
from application.service import auth_service
from flask_jwt import JWT, jwt_required, current_identity

application = create_app('default')
db.init_app(application)


@application.before_first_request
def create_tables():
    db.create_all()
    if role_repository.get_by_name("admin") is None:
        role_repository.add_new("admin")
        role_repository.add_new('user')
        user_repository.add_new("Потапов", "Дмитрий", "Иванович", "root", "root", 1)


@application.after_request
def after_request_func(response):
    res_data = response.json
    try:
        access_token = res_data['access_token']
        response.headers['Authorization'] = "JWT " + access_token
    except Exception as ex:
        print(ex)
    finally:
        return response


jwt = JWT(application, auth_service.authenticate, auth_service.identity)

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=5020)
