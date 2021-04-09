from .repository import category_repository


def add_new_category(data):
    parent_id = data["parent_category_id"]
    data.pop("parent_category_id")
    data.pop("parent_name")
    if parent_id is None:
        data["children"] = []
        data["root"] = True
        category_repository.category_create(data)
    else:
        category_repository.add_child(parent_id, data)
        data['root'] = False
        data["children"] = []
        category_repository.category_create(data)


def update_category(data):
    parent_id = data["parent_category_id"]
    data.pop("parent_category_id")
    data.pop("parent_name")
    current_cat_id = data['category_id']
    categories = category_repository.get_all_category()
    current_cat_json = category_repository.get_category_by_id(current_cat_id)
    current_cat_json.pop('children')
    current_cat_json.pop('root')
    for cat in categories:
        if not cat["isNil"]:
            if current_cat_json in cat['children']:
                cat_child_arr = cat['children']
                cat_child_arr.remove(current_cat_json)
                category_repository.update_child(cat['category_id'], cat_child_arr)
                break
    if parent_id is not None:
        category_repository.add_child(parent_id, data)
        data['root'] = False
    else:
        data['root'] = True
    current_cat_json = category_repository.get_category_by_id(current_cat_id)
    children_arr = current_cat_json["children"]
    data['children'] = children_arr
    category_repository.category_update(data)


def delete_category(category_id):
    categories = category_repository.get_all_category()
    current_cat_json = category_repository.get_category_by_id(category_id)
    current_cat_json.pop('children')
    for cat in categories:
        if not cat["isNil"]:
            if current_cat_json in cat['children']:
                cat_child_arr = cat['children']
                cat_child_arr.remove(current_cat_json)
                category_repository.update_child(cat['category_id'], cat_child_arr)
                break
    category_repository.category_delete(category_id)
