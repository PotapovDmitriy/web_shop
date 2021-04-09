from flask import Flask
import sys

sys.path.append("../../..")


def create_app(config_name):
    app = Flask(__name__)
    # app.config["MONGO_URI"] = 'mongodb://admin:root@db_mongo:27017/test'

    app.secret_key = "123456"
    from .routs.category_routs import category_routs
    app.register_blueprint(category_routs)

    return app
