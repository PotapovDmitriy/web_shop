from flask import Flask
import logging
import sys

sys.path.append("../..")


# Разработка_веб_приложений_с_использованием_Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db_mysql:3306/web_shop'
    app.config["SQLALCHEMY_POOL_SIZE"] = 30
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 5
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 2
    app.config["SQLALCHEMY_MAX_OVERFLOW"] = -1
    app.config["SESSION_COOKIE_SAMESITE"] = 'None'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "123456"

    from .routs.admin_routs import admin_routs

    app.register_blueprint(admin_routs)

    return app
