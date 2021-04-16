from flask import Flask
import sys

sys.path.append("../..")


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/web_shop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "123456"

    from .routs.buyer_routs import buyer_routs
    from .routs.admin_routs import admin_routs
    #
    app.register_blueprint(buyer_routs)
    app.register_blueprint(admin_routs)

    return app
