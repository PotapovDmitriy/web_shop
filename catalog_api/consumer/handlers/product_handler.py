from .repository import category_repository


def add_new_product(data):
    cat_id = data["category_id"]
    data.pop("category_id")
    data.pop("category_name")
    category_repository.add_child(cat_id, data)


def update_product(data):
    cat_id = data["category_id"]
    product_id = data['product_id']
    data.pop("category_id")
    category = category_repository.get_category_by_id(cat_id)
    products_arr = category['children']
    for product in products_arr:
        if product['product_id'] == product_id:
            products_arr.remove(product)
            category_repository.update_child(cat_id, products_arr)
    category_repository.add_child(cat_id, data)


def delete_product(product_id):
    categories = category_repository.get_all_category()
    for category in categories:
        if category['isNil']:
            cat_id = category['category_id']
            products_arr = category['children']
            for product in products_arr:
                if product['product_id'] == product_id:
                    products_arr.remove(product)
                    category_repository.update_child(cat_id, products_arr)
                    return True
