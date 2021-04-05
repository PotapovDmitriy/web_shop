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
    data = json_body['data']
    if type_number == 1:
        conn_str = "http://catalog_api:5010/new_category"
    elif type_number == 2:
        conn_str = "http://catalog_api:5010/new_product"
    elif type_number == 3:
        conn_str = "http://catalog_api:5010/redact_category"
    elif type_number == 4:
        conn_str = "http://catalog_api:5010/redact_product"
    elif type_number == 5:
        print(data)
        conn_str = "http://catalog_api:5010/delete_category?id=" + str(data["id"])
    elif type_number == 6:
        print(data)
        conn_str = "http://catalog_api:5010/delete_product?id=" + str(data["id"])
    if type_number > 4:
        requests.post(conn_str, json=data)
    else:
        requests.post(conn_str, json=data)


channel.basic_consume(queue='app_que', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
