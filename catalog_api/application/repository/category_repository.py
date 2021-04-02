from ..connector import categories_collection


def category_create(insert_category) -> None:
    categories_collection.insert_one(insert_category)


def category_update(update_category) -> None:
    categories_collection.update({"category_id": update_category["category_id"]}, update_category)


def category_delete(remove_category) -> None:
    categories_collection.remove({"category_id": remove_category["category_id"]})


def get_category_by_id(category_id) -> {}:
    return categories_collection.find_one({"category_id": category_id}, {"_id": 0})


def get_all_root_category() -> []:
    results = categories_collection.find({"parent_category_id": None}, {"_id": 0})
    return [r for r in results]


def get_all_children_category(category_id) -> []:
    results = categories_collection.find({"parent_category_id": category_id}, {"_id": 0})
    return [r for r in results]
