import pika
import json
from handlers import order_handler

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='app_que_order', durable=True)
channel.exchange_declare(exchange='app_que_ex_order', exchange_type='fanout')

channel.queue_bind(exchange='app_que_ex_order', queue='app_que_order')


def callback(ch, method, properties, body):
    json_body = json.loads(body.decode())
    type_number = int(json_body['type_number'])
    user_id = json_body['user_id']
    products = json_body['products']
    if type_number == 1:
        order_handler.create_new_order(user_id, products)



channel.basic_consume(queue='app_que_order', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
