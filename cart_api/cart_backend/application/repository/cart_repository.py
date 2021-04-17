from ..connector import cart_collection


def get_cart_by_user_id(user_id) -> {}:
    return cart_collection.find_one({"user_id": user_id}, {"_id": False})


def get_all_carts() -> []:
    results = cart_collection.find({}, {'_id': False})
    return [r for r in results]


def cart_create(insert_cart) -> None:
    cart_collection.insert_one(insert_cart)


def cart_update(update_cart) -> None:
    cart_collection.update({"user_id": update_cart["user_id"]}, update_cart)


def add_child(user_id, children_json) -> None:
    parent_json = get_cart_by_user_id(user_id)
    parent_json["products"].append(children_json)
    cart_update(parent_json)


def update_child(user_id, products_arr) -> None:
    parent_json = get_cart_by_user_id(user_id)
    parent_json["products"] = products_arr
    cart_update(parent_json)


def delete_product(user_id, product_id) -> bool:
    cart = get_cart_by_user_id(user_id)
    products_arr = cart['products']
    for product in products_arr:
        if product['product_id'] == product_id:
            products_arr.remove(product)
            update_child(user_id, products_arr)
            return True
    return False
