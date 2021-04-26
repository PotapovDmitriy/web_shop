import requests

ORDER_API = "http://order_api:5018/"


def create_new_order(user_id, products):
    json = {"user_id": user_id, "products": products}
    print(json)
    requests.post(ORDER_API + "new_order", json=json)
