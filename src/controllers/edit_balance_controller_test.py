from src.controllers.edit_balance_controller import EditBalanceController

class MockUsersRepository:
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        return None

def test_edit_balance_controller():
    edit_balance_controller = EditBalanceController(MockUsersRepository())
    response = edit_balance_controller.edit_balance(1, 100)
    assert response["status"] == "success"
    assert response["message"] == "Balance updated successfully"
    assert response["new_balance"] == 100
