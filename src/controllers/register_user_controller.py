from src.models.interfaces.users_repository_interface import UsersRepositoryInterface
from src.drivers.password_handler import PasswordHandler

class RegisterUserController:
    def __init__(self, users_repository: UsersRepositoryInterface, password_handler: PasswordHandler):
        self.__users_repository = users_repository
        self.__password_handler = password_handler

    def register_user(self, username: str, password: str) -> None:
        hashed_password = self.__password_handler.encrypt_password(password)
        self.__users_repository.register_user(username, hashed_password)

