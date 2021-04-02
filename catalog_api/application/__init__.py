from flask import Flask
import sys

sys.path.append("../..")


def create_app(config_name):
    app = Flask(__name__)

    app.secret_key = "123456"

    from .routs.product_routs import product_routs
    from .routs.category_routs import category_routs

    app.register_blueprint(product_routs)
    app.register_blueprint(category_routs)

    return app
