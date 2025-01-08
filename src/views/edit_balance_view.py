from src.controllers.interfaces.edit_balance_controller_interface import EditBalanceControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class EditBalanceView(ViewInterface):
    def __init__(self, edit_balance_controller: EditBalanceControllerInterface) -> None:
        self.edit_balance_controller = edit_balance_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body['new_balance']
        user_id = http_request.body['user_id']
        self.__validate_inputs(user_id, new_balance)
        response = self.edit_balance_controller.edit_balance(user_id, new_balance)
        return HttpResponse(status_code=200, body={"data": response})
    
    def __validate_inputs(self, user_id: any, new_balance: any) -> None:
        if (
            not user_id 
            or not new_balance 
            or not isinstance(user_id, int) 
            or not isinstance(new_balance, float)
        ): raise Exception('Invalid inputs')