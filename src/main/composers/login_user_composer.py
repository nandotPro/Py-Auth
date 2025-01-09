from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.login_user_controller import LoginUserController
from src.views.login_user_view import LoginUserView

def login_user_composer():
    model = UsersRepository(db_connection_handler.get_connection())
    controller = LoginUserController(model)
    view = LoginUserView(controller)
    return view