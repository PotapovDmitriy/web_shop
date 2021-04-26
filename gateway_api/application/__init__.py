from flask import Flask
import sys

sys.path.append("../..")


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_mysql:3306/web_shop_users'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "123456"

    from .routs.buyer_routs import buyer_routs
    from .routs.admin_routs import admin_routs
    from .routs.cart_routs import cart_routs
    from .routs.auth_routs import auth_routs
    from .routs.order_routs import order_routs
    #
    app.register_blueprint(buyer_routs)
    app.register_blueprint(admin_routs)
    app.register_blueprint(cart_routs)
    app.register_blueprint(auth_routs)
    app.register_blueprint(order_routs)

    return app
