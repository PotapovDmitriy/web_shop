from .connector import categories_collection


def category_create(insert_category) -> None:
    categories_collection.insert_one(insert_category)


def category_update(update_category) -> None:
    categories_collection.update({"category_id": update_category["category_id"]}, update_category)


def category_delete(category_id) -> None:
    categories_collection.remove({"category_id": category_id})


def get_category_by_id(category_id) -> {}:
    return categories_collection.find_one({"category_id": category_id}, {"_id": False})


def add_child(parent_id, children_json) -> None:
    parent_json = get_category_by_id(parent_id)
    parent_json["children"].append(children_json)
    category_update(parent_json)


def get_all_category() -> []:
    results = categories_collection.find({}, {'_id': False})
    return [r for r in results]


def update_child(parent_id, children_arr) -> None:
    parent_json = get_category_by_id(parent_id)
    parent_json["children"] = children_arr
    category_update(parent_json)
