from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.edit_balance_controller import EditBalanceController
from src.views.edit_balance_view import EditBalanceView

def edit_balance_composer():
    model = UsersRepository(db_connection_handler.get_connection())
    controller = EditBalanceController(model)
    view = EditBalanceView(controller)
    return view