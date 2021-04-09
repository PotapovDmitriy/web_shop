from application import create_app
# from application.connector import mongo

application = create_app('default')
# mongo.init_app(application)



if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=5010)


