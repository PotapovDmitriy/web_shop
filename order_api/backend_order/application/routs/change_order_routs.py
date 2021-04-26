from flask import Blueprint, request
from flask_cors import cross_origin
from ..repository import event_repository, order_reposetory, snapshot_repository
from ..service import help_service

order_routs = Blueprint('order_routs', __name__)


@order_routs.route('/cancel_order', methods=['POST'])
@cross_origin(supports_credentials=True)
def create_new_order():
    try:
        json_body = request.json
        user_role = int(json_body['role_id'])
        order_id = json_body["order_id"]
        event_arr = event_repository.get_by_order(order_id)
        max_val = 0
        last_event = None

        for event in event_arr:
            if event.version > max_val:
                max_val = event.version
                last_event = event
        if last_event.status != "created":
            if last_event.status != "confirm":
                return {"msg": "this order cannot be canceled"}
        if user_role == 1:
            event_repository.add_new(order_id, last_event.version + 1, "canceled by admin")
        else:
            event_repository.add_new(order_id, last_event.version + 1, 'canceled by user')
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@order_routs.route('/confirm_order', methods=['POST'])
@cross_origin(supports_credentials=True)
def confirm_order():
    try:
        json_body = request.json
        user_role = int(json_body['role_id'])
        order_id = json_body["order_id"]
        last_event = help_service.find_last_event(order_id)
        if last_event.status != "created":
            return {"msg": "this order cannot be confirmed"}
        if user_role == 1:
            event_repository.add_new(order_id, last_event.version + 1, "confirm")
        else:
            return {"msg": 'you have no permission'}
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@order_routs.route('/execute_order', methods=['POST'])
@cross_origin(supports_credentials=True)
def execute_order():
    try:
        json_body = request.json
        user_role = int(json_body['role_id'])
        order_id = json_body["order_id"]
        last_event = help_service.find_last_event(order_id)
        if last_event.status != "confirm":
            return {"msg": "this order cannot be executed"}
        if user_role == 1:
            event_repository.add_new(order_id, last_event.version + 1, "execute")
        else:
            return {"msg": 'you have no permission'}
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


