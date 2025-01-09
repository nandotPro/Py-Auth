from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composers.register_user_composer import register_user_composer
from src.main.composers.login_user_composer import login_user_composer
from src.main.composers.edit_balance_composer import edit_balance_composer

user_routes_bp = Blueprint('user_routes', __name__)

@user_routes_bp.route('/register', methods=['POST'])
def register_user():
    http_request = HttpRequest(body=request.json)
    view  = register_user_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route('/login', methods=['POST'])
def login_user():
    http_request = HttpRequest(body=request.json)
    view  = login_user_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route('/edit_balance/<int:user_id>', methods=['POST'])
def edit_balance(user_id):
    http_request = HttpRequest(body=request.json, params={"user_id": user_id})
    view  = edit_balance_composer()
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
