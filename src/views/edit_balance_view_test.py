from src.views.edit_balance_view import EditBalanceView
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
import pytest

class MockController:
    def edit_balance(self, user_id: int, new_balance: float) -> str:
        return "Balance edited successfully"
    
def test_edit_balance_view():
    body = {
        "new_balance": 100.0
    }
    params = {
        "user_id": 1
    }
    request = HttpRequest(body=body, params=params)
    response = EditBalanceView(MockController()).handle(request)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {"data": "Balance edited successfully"}

def test_edit_balance_view_invalid_inputs():
    body = {
        "new_balance": 100.0
    }
    params = {
        "user_id": "1"
    }
    request = HttpRequest(body=body, params=params)
    with pytest.raises(Exception):
        EditBalanceView(MockController()).handle(request)
