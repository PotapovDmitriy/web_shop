from flask import Flask
import logging
import sys

sys.path.append("../../..")


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_mysql:3306/web_shop_users'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:user@localhost:5432/web_shop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "123456"

    from .routs.change_order_routs import order_routs
    from .routs.order_consumer_routs import consumer_routs
    from .routs.represent_order_routs import repr_order_routs
    #
    app.register_blueprint(order_routs)
    app.register_blueprint(consumer_routs)
    app.register_blueprint(repr_order_routs)

    return app
