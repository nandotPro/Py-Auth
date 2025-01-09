from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.login_user_controller import LoginUserController
from src.views.login_user_view import LoginUserView
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JwtHandler

def login_user_composer():
    model = UsersRepository(db_connection_handler.get_connection())
    password_handler = PasswordHandler()
    jwt_handler = JwtHandler()
    controller = LoginUserController(model, password_handler, jwt_handler)
    view = LoginUserView(controller)
    return view