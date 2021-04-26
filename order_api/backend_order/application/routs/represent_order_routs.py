from flask import Blueprint, request
from flask_cors import cross_origin
from ..repository import event_repository, order_reposetory, snapshot_repository
from ..service import help_service

repr_order_routs = Blueprint('repr_order_routs', __name__)


@repr_order_routs.route('/all_orders', methods=['POST'])
@cross_origin(supports_credentials=True)
def get_all_orders():
    try:
        json_body = request.json
        user_role = int(json_body['role_id'])
        user_id = json_body["user_id"]
        result = []
        if user_role == 1:
            all_orders = order_reposetory.get_all()
        else:
            all_orders = order_reposetory.get_by_owner(user_id)
        for order in all_orders:
            last_event = help_service.find_last_event(order.id)
            snap = snapshot_repository.get_by_order(order.id)
            new_data = help_service.apply_events(order.id)
            snapshot_repository.update(snap, last_event.version, str(new_data))
            new_data['order_id'] = order.id
            result.append(new_data)
        return {"orders": result}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@repr_order_routs.route('/get_order', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_order():
    try:
        order_id = int(request.args.get("id"))
        last_event = help_service.find_last_event(order_id)
        snap = snapshot_repository.get_by_order(order_id)
        new_data = help_service.apply_events(order_id)
        new_snap = snapshot_repository.update(snap, last_event.version, str(new_data))
        return new_snap.to_json()
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
