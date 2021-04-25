import json
import pika


def send_message_for_item(user_id, data):
    credentials = pika.PlainCredentials('user', 'user')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='app_que_ex_order',
                             exchange_type='fanout')

    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # channel = connection.channel()
    # channel.queue_declare(queue="app_que")
    print(str(data))
    channel.basic_publish(exchange='app_que_ex_order',
                          routing_key='app_que_order',
                          body=json.dumps({"user_id": user_id,
                                           "data": data,
                                           "type_number": 1}))

    print(" [x] Sent text for update key words in project")
    connection.close()
