from flask import Blueprint, render_template, request, redirect, url_for

from ..database import db
from ..repository import category_repository
from ..messages import message

category_routs = Blueprint('category_routs', __name__)


@category_routs.route('/new_category', methods=['POST'])
def create_category():
    try:
        if request.method == "POST":
            json_body = request.json
            name = json_body['name']
            parent_id = json_body["parent_category_id"]
            if parent_id is not None:
                parent = category_repository.get_by_id(parent_id)
                if parent.nil:
                    return {"msg": "Parent can not be nil!"}
            is_nil = json_body['isNil']
            new_category = category_repository.add_new(name, parent_id, is_nil)
            message.send_message_for_item(new_category.to_json(), 1)
            return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@category_routs.route('/categories', methods=['GET'])
def get_categories():
    try:
        all_categories = category_repository.get_all()
        data_json = []
        for cat in all_categories:
            data_json.append(cat.to_json())
        return {"categories": data_json}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@category_routs.route('/category', methods=['GET'])
def get_category():
    try:
        category_id = request.args.get("id")
        category = category_repository.get_by_id(category_id)

        return category.to_json()
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@category_routs.route('/delete_category', methods=['GET'])
def delete_category():
    try:
        category_id = request.args.get("id")
        category = category_repository.get_by_id(category_id)
        if len(category.products) != 0 or len(category.get_children_if_exist()) != 0:
            return {
                "msg": "can not be deleted, have children"
            }
        msg = category_repository.delete(category)
        message.send_message_for_item({"id": category_id}, 5)
        return {"msg": msg}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()


@category_routs.route('/redact_category', methods=['POST'])
def redact_category():
    try:
        json_body = request.json
        category_id = json_body['category_id']
        name = json_body['name']
        is_nil = json_body['isNil']
        # Вот тут надо подумать, принимать название категории или ее id
        parent_category_id = json_body['parent_category_id']
        category = category_repository.get_by_id(category_id)
        if parent_category_id:
            parent = category_repository.get_by_id(parent_category_id)
            if parent.nil:
                return {"msg": "Parent can not be nil!"}

        if not category.can_be_nil() and is_nil:
            return {'msg': "Category cant be nil"}

        updated_category = category_repository.update(category, name, parent_category_id, is_nil)

        message.send_message_for_item(updated_category.to_json(), 3)
        return str(True)
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
    finally:
        db.session.close()
