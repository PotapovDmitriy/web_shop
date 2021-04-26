from ..repository import event_repository, order_reposetory, snapshot_repository
import json


def find_last_event(order_id):
    event_arr = event_repository.get_by_order(order_id)
    max_val = 0
    last_event = None
    for event in event_arr:
        if event.version > max_val:
            max_val = event.version
            last_event = event
    return last_event


def apply_events(order_id):
    last_snapshot = snapshot_repository.get_by_order(order_id)
    last_event = find_last_event(order_id)
    if last_event.version == last_snapshot.version:
        data = str(last_snapshot.data).replace("\'", "\"")
        return json.loads(data)
    else:
        data = json.loads(str(last_snapshot.data).replace("\'", "\""))
        data["status"] = last_event.status
        return data

