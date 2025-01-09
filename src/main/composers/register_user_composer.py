from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.register_user_controller import RegisterUserController
from src.views.register_user_view import RegisterUserView

def register_user_composer():
    model = UsersRepository(db_connection_handler.get_connection())
    controller = RegisterUserController(model)
    view = RegisterUserView(controller)
    return view