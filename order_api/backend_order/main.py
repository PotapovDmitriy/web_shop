from application import create_app
from application.database import db


application = create_app('default')
db.init_app(application)
with application.app_context():
    # from application.models.event import Event
    # from application.models.order import Order
    # from application.models.snapshot import Snapshot
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
    # consumer = OrderConsumer()
    # consumer.start_consuming_thread()
    application.run(debug=True, host="0.0.0.0", port=5018)
