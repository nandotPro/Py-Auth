from src.controllers.register_user_controller import RegisterUserController
from src.drivers.password_handler import PasswordHandler

class MockUsersRepository:
    def __init__(self):
        self.register_user_attributes = {}

    def register_user(self, username: str, password: str) -> None:
        self.register_user_attributes["username"] = username
        self.register_user_attributes["password"] = password

def test_register_user_controller():
    repository = MockUsersRepository()
    controller = RegisterUserController(repository, PasswordHandler())
    response = controller.register_user("John Doe", "123456")
    assert response["type"] == "User"
    assert response["username"] == "John Doe"
    assert repository.register_user_attributes["username"] == "John Doe"
    assert repository.register_user_attributes["password"] != "123456"
