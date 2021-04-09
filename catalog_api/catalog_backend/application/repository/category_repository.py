from ..connector import categories_collection


def get_category_by_id(category_id) -> {}:
    return categories_collection.find_one({"category_id": category_id}, {"_id": False})


def get_all_root_category() -> []:
    results = categories_collection.find({"root": True}, {"_id": False})

    return [r for r in results]


def get_all_children(category_id) -> []:
    category = get_category_by_id(category_id)
    return category['children']


def get_all_category() -> []:
    results = categories_collection.find({}, {'_id': False})
    return [r for r in results]
