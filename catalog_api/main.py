from application import create_app

application = create_app('default')

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=5010)

