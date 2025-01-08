from src.models.interfaces.users_repository_interface import UsersRepositoryInterface
from src.controllers.interfaces.edit_balance_controller_interface import EditBalanceControllerInterface


class EditBalanceController(EditBalanceControllerInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def edit_balance(self, user_id: int, new_balance: float) -> dict:
        self.__users_repository.edit_balance(user_id, new_balance)
        return {
            "status": "success",
            "message": "Balance updated successfully",
            "new_balance": new_balance
        }
