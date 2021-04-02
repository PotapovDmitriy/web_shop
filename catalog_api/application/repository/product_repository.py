from ..connector import products_collection


def product_create(insert_product) -> None:
    products_collection.insert_one(insert_product)


def product_update(update_product) -> None:
    products_collection.update({"product_id": update_product["product_id"]}, update_product)


def product_delete(product_id) -> None:
    products_collection.remove({"product_id": product_id})


def get_product_by_id(product_id) -> {}:
    return products_collection.find_one({"product_id": product_id}, {"_id": 0})


def get_products_by_category_id(category_id) -> []:
    results = products_collection.find({"category_id": category_id}, {"_id": 0})
    return [r for r in results]
