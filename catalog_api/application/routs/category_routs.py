from flask import Blueprint, render_template, request, redirect, url_for

from ..repository import category_repository

category_routs = Blueprint('category_routs', __name__)


@category_routs.route('/new_category', methods=['POST'])
def create_category():
    try:
        json_body = request.json
        category_repository.category_create(json_body)
        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/root_categories', methods=['GET'])
def get_categories():
    try:
        all_categories = category_repository.get_all_root_category()
        return {"categories": all_categories}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/children_categories', methods=['GET'])
def get_categories():
    try:
        category_id = request.args.get("category_id")
        all_categories = category_repository.get_all_children_category(category_id)
        return {"categories": all_categories}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/category', methods=['GET'])
def get_category():
    try:
        category_id = request.args.get("id")
        category_json = category_repository.get_category_by_id(category_id)

        return category_json
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/delete_category ', methods=['GET'])
def delete_category():
    try:
        category_id = request.args.get("id")
        category_repository.category_delete(category_id)

        return {"msg": True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/redact_category', methods=['POST'])
def redact_category():
    try:
        json_body = request.json

        category_repository.category_update(json_body)
        return {'msg': True}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
