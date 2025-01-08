from src.views.login_user_view import LoginUserView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
import pytest

class MockController:
    def login_user(self, username: str, password: str) -> str:
        return "User logged in successfully"
    
def test_login_user_view():
    body = {
        "username": "John Doe",
        "password": "123456"
    }
    request = HttpRequest(body=body)
    response = LoginUserView(MockController()).handle(request)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {"data": "User logged in successfully"}

def test_login_user_view_invalid_inputs():
    body = {
        "username": "John Doe",
        "password": 123456
    }
    request = HttpRequest(body=body)
    with pytest.raises(Exception):
        LoginUserView(MockController()).handle(request)

