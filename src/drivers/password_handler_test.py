from src.drivers.password_handler import PasswordHandler
import pytest

@pytest.fixture
def password_handler():
    return PasswordHandler()

def test_encrypt_password(password_handler):
    password = "123456"
    hashed_password = password_handler.encrypt_password(password)
    assert hashed_password != password

def test_check_password(password_handler):
    password = "123456"
    hashed_password = password_handler.encrypt_password(password)
    assert password_handler.check_password(password, hashed_password)
    