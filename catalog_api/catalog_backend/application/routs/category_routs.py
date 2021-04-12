from flask import Blueprint, request
from flask_cors import cross_origin

from ..repository import category_repository

category_routs = Blueprint('category_routs', __name__)


@category_routs.route('/root_categories', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_root_categories():
    try:
        all_categories = category_repository.get_all_root_category()
        return {"categories": all_categories}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/children', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_children_categories():
    try:
        category_id = int(request.args.get("category_id"))
        all_categories = category_repository.get_all_children(category_id)
        return {"categories": all_categories}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)


@category_routs.route('/category', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_category():
    try:
        category_id = int(request.args.get("id"))
        category_json = category_repository.get_category_by_id(category_id)
        return category_json if category_json else {"msg": "Empty"}
    except Exception as ex:
        return ({
                    'ERROR': str(ex)
                }, 400)
