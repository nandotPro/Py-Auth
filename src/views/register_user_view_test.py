from src.views.register_user_view import RegisterUserView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
import pytest

class MockController:
    def register_user(self, username: str, password: str) -> str:
        return "User registered successfully"

def test_register_user_view():
    body = {
        "username": "John Doe",
        "password": "123456"
    }
    request = HttpRequest(body=body)
    response = RegisterUserView(MockController()).handle(request)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body == {"data": "User registered successfully"}

def test_register_user_view_invalid_inputs():
    body = {
        "username": "John Doe",
        "password": 123456
    }
    request = HttpRequest(body=body)
    with pytest.raises(Exception):
        RegisterUserView(MockController()).handle(request)
    