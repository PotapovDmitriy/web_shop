from .repository import cart_repository


def update_product(data):
    product_id = data['product_id']
    data.pop("category_id")
    all_carts = cart_repository.get_all_carts()
    for cart in all_carts:
        user_id = cart['user_id']
        products_arr = cart['products']
        for product in products_arr:
            if product['product_id'] == product_id:
                products_arr.remove(product)
                cart_repository.update_child(user_id, products_arr)
        cart_repository.add_child(user_id, data)


def delete_product(product_id):
    carts = cart_repository.get_all_carts()
    for cart in carts:
        user_id = cart['user_id']
        products_arr = cart['products']
        for product in products_arr:
            if product['product_id'] == product_id:
                products_arr.remove(product)
                cart_repository.update_child(user_id, products_arr)
                return True
