import pika
import json
from handlers import catalog_handler, product_handler

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='app_que', durable=True)
channel.exchange_declare(exchange='app_que_ex', exchange_type='fanout')

channel.queue_bind(exchange='app_que_ex', queue='app_que')


def callback(ch, method, properties, body):
    json_body = json.loads(body.decode())
    type_number = json_body['type']
    data = json_body['data']
    if type_number == 1:
        catalog_handler.add_new_category(data)
    elif type_number == 2:
        product_handler.add_new_product(data)
    elif type_number == 3:
        catalog_handler.update_category(data)
    elif type_number == 4:
        product_handler.update_product(data)
    elif type_number == 5:
        catalog_handler.delete_category(int(data["id"]))
    elif type_number == 6:
        product_handler.delete_product(int(data["id"]))


channel.basic_consume(queue='app_que', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
