from flask import Flask
import sys

sys.path.append("../..")


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_mysql:3306/web_shop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "123456"

    # from .routs.product_routs import product_routs
    # from .routs.category_routs import category_routs
    #
    # app.register_blueprint(product_routs)
    # app.register_blueprint(category_routs)

    return app
