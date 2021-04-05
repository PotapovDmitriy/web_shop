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
    channel.basic_publish(exchange='app_que_ex',
                          routing_key='app_que',
                          body=json.dumps({"type": type_number,
                                           "data": data}))

    print(" [x] Sent text for update key words in project")
    connection.close()
