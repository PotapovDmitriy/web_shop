import pika
import requests
import json
from datetime import timedelta

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='app_que', durable=True)
channel.exchange_declare(exchange='app_que_ex', exchange_type='fanout')

channel.queue_bind(exchange='app_que_ex', queue='app_que')

def callback(ch, method, properties, body):
    json_body = json.loads(body.decode())
    type_number = json_body['type']
    json_body = json.loads(body.decode())

    conn_str = "http://catalog_api:5010/new_product"
    data = json_body['data']
    requests.post(conn_str, json=data)


channel.basic_consume(queue='app_que', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
