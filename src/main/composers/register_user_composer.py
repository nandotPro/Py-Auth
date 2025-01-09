from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.register_user_controller import RegisterUserController
from src.views.register_user_view import RegisterUserView
from src.drivers.password_handler import PasswordHandler

def register_user_composer():
    model = UsersRepository(db_connection_handler.get_connection())
    password_handler = PasswordHandler()
    controller = RegisterUserController(model, password_handler)
    view = RegisterUserView(controller)
    return view