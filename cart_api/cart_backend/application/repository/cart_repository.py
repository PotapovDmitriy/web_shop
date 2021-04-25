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
    products = parent_json['products']
    flag = True
    for product in products:
        if product['product_id'] == children_json['product_id']:
            price = int(product["price"]) / product['count']
            product['price'] = int(product['price']) + int(price)
            product['count'] += 1
            flag = False
            break
    if flag:
        children_json["count"] = 1
        parent_json["products"].append(children_json)
    parent_json['full_price'] += children_json['price']
    cart_update(parent_json)


def update_child(user_id, products_arr) -> None:
    parent_json = get_cart_by_user_id(user_id)
    parent_json["products"] = products_arr
    cart_update(parent_json)


def delete_product(user_id, product_id) -> bool:
    cart = get_cart_by_user_id(user_id)
    products_arr = cart['products']
    deleted_price = 0
    for product in products_arr:
        if product['product_id'] == product_id:
            deleted_price = int(product['price'])
            products_arr.remove(product)
            cart['full_price'] -= deleted_price
            cart_update(cart)
            update_child(user_id, products_arr)
            return True
    return False


def get_count_minus_1(user_id, product_id) -> bool:
    cart = get_cart_by_user_id(user_id)
    products_arr = cart['products']
    for product in products_arr:
        if product['product_id'] == product_id:
            price = int(product["price"]) / product['count']
            if int(product['count']) == 1:
                return delete_product(user_id, product_id)
            product["count"] -= 1
            product["price"] = int(price) * product['count']
            update_child(user_id, products_arr)
            cart["full_price"] -= price
            cart_update(cart)
            return True

    return False


def clear_cart(cart):
    cart["products"] = []
    cart['full_price'] = 0
    cart_update(cart)
    return True
