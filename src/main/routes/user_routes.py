from flask import Blueprint, jsonify
from src.views.register_user_view import RegisterUserView


user_routes_bp = Blueprint('user_routes', __name__)

@user_routes_bp.route('/register', methods=['POST'])
def register_user():
    # try:
    #     request = HttpRequest(body=request.json)
    #     view  = register_user_composer()
    #     response = view.handle(request)
    #     return jsonify(response.body), response.status_code
    # except Exception as e:
    #     reponse = handle_error(e)
    #     return jsonify(reponse.body), reponse.status_code

