from src.models.interfaces.users_repository_interface import UsersRepositoryInterface
from src.drivers.password_handler import PasswordHandler

class RegisterUserController:
    def __init__(self, users_repository: UsersRepositoryInterface, password_handler: PasswordHandler):
        self.__users_repository = users_repository
        self.__password_handler = password_handler

    def register_user(self, username: str, password: str) -> dict:
        hashed_password = self.__hash_password(password)
        self.__register_user_in_database(username, hashed_password)
        return self.__format_response(username)
    
    def __hash_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)
        return hashed_password
    
    def __register_user_in_database(self, username: str, hashed_password: str) -> None:
        self.__users_repository.register_user(username, hashed_password)
    
    def __format_response(self, username: str) -> dict:
        return {
            "type": "User",
            "username": username,
        }
