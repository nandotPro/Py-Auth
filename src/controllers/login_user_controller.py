from src.models.interfaces.users_repository_interface import UsersRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JwtHandler
from src.controllers.interfaces.login_user_controller_interface import LoginUserControllerInterface


class LoginUserController(LoginUserControllerInterface):
    def __init__(self, users_repository: UsersRepositoryInterface, password_handler: PasswordHandler, jwt_handler: JwtHandler):
        self.__users_repository = users_repository
        self.__password_handler = password_handler
        self.__jwt_handler = jwt_handler

    def login_user(self, username: str, password: str) -> dict:
        user = self.__get_user_by_username(username)
        user_id = user[0]
        hashed_password = user[2]
        self.__verify_password(password, hashed_password)
        token = self.__create_jwt_token({"user_id": user_id})
        return self.__format_response(username, token)
    

    def __get_user_by_username(self, username: str) -> tuple[int, str, float]:
        user = self.__users_repository.get_user_by_username(username)
        if not user:
            raise ValueError("User not found")
        return user
    
    def __verify_password(self, password: str, hashed_password: str) -> None:
        correct_password = self.__password_handler.check_password(password, hashed_password)
        if not correct_password:
            raise ValueError("Wrong password")
    
    def __create_jwt_token(self, user_id: int) -> str:
        return self.__jwt_handler.create_jwt_token({"user_id": user_id})

    def __format_response(self, username: str, token: str) -> dict:
        return {
            "access": True,
            "username": username,
            "auth_token": token
        }

