from src.drivers.password_handler import PasswordHandler
from src.controllers.login_user_controller import LoginUserController
from src.drivers.jwt_handler import JwtHandler
import pytest

username = "John Doe"
password = "123456"
hashed_password = PasswordHandler().encrypt_password(password)

class MockUsersRepository:
    def get_user_by_username(self, username: str) -> tuple[int, str, float]:
        return (1, username, hashed_password)

def test_login_user_controller():
    login_user_controller = LoginUserController(MockUsersRepository(), PasswordHandler(), JwtHandler())
    response = login_user_controller.login_user(username, password)
    assert response["access"] == True
    assert response["username"] == username
    assert response["auth_token"] is not None

def test_login_user_controller_with_wrong_password():
    login_user_controller = LoginUserController(MockUsersRepository(), PasswordHandler(), JwtHandler())
    with pytest.raises(ValueError):
        login_user_controller.login_user(username, "fake_password")
