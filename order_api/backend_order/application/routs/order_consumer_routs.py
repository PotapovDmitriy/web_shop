from flask import Blueprint, request
from flask_cors import cross_origin
import requests
import json
from ..repository import order_reposetory, event_repository, snapshot_repository

consumer_routs = Blueprint('cons_routs', __name__)


@consumer_routs.route('/new_order', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_new_order():
    try:
        json_body = request.json
        user_id = json_body['user_id']
        products = json_body['products']
        print(json_body)
        new_order = order_reposetory.add_new(user_id)
        new_event = event_repository.add_new(new_order.id, 1, "created")
        data = {'status': "created", "products": products}
        snapshot_repository.add_new(new_order.id, new_event.version, str(data))

        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
