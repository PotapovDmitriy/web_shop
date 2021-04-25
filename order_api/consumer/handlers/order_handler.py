from .repository import order_reposetory, snapshot_repository, event_repository


def create_new_order(user_id, products):
    new_order = order_reposetory.add_new(user_id)
    event_repository.add_new(new_order.id, 1, "created")
    data = {'status': "created", "products": products}
    snapshot_repository.add_new(new_order.id, 1, data)
