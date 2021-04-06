from application import create_app
from application.database import db

application = create_app('default')
db.init_app(application)
# db.create_all()

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0")

