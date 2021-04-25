from order_api.backend_order.application import create_app
from order_api.backend_order.application import db

application = create_app('default')
db.init_app(application)
with application.app_context():
    db.create_all()


@application.after_request
def after_request_func(response):
    try:
        return response
    except Exception as ex:
        print(ex)
    finally:
        db.session.close()


if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=5018)
