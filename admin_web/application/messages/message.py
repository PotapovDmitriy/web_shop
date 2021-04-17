import json
import pika


def send_message_for_item(data, type_number):
    credentials = pika.PlainCredentials('user', 'user')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='app_que_ex',
                             exchange_type='fanout')

    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # channel = connection.channel()
    # channel.queue_declare(queue="app_que")
    print(str(data))
    channel.basic_publish(exchange='app_que_ex',
                          routing_key='app_que',
                          body=json.dumps({"type": type_number,
                                           "data": data}))

    channel.exchange_declare(exchange='app_que_ex_cart',
                             exchange_type='fanout')

    # channel.queue_declare(queue="app_que_cart")
    if type_number == 4 or type_number == 6:
        channel.basic_publish(exchange='app_que_ex_cart',
                              routing_key='cart_que',
                              body=json.dumps({"type": type_number,
                                               "data": data}))

    print(" [x] Sent text for update key words in project")
    connection.close()
