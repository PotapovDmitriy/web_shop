import pika
import json
from handlers import cart_handler

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='app_que_cart', durable=True)
channel.exchange_declare(exchange='app_que_ex_cart', exchange_type='fanout')

channel.queue_bind(exchange='app_que_ex_cart', queue='app_que_cart')


def callback(ch, method, properties, body):
    json_body = json.loads(body.decode())
    type_number = json_body['type']
    data = json_body['data']
    if type_number == 4:
        cart_handler.update_product(data)
    elif type_number == 6:
        cart_handler.delete_product(int(data["id"]))


channel.basic_consume(queue='app_que_cart', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
