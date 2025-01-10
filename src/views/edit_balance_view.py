from src.controllers.interfaces.edit_balance_controller_interface import EditBalanceControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.errors_types.http_bad_request import HttpBadRequestError

class EditBalanceView(ViewInterface):
    def __init__(self, edit_balance_controller: EditBalanceControllerInterface) -> None:
        self.edit_balance_controller = edit_balance_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body['new_balance']
        user_id = http_request.params['user_id']
        
        if isinstance(new_balance, (str, int)):
            new_balance = float(new_balance)
            
        self.__validate_inputs(user_id, new_balance)
        response = self.edit_balance_controller.edit_balance(user_id, new_balance)
        return HttpResponse(status_code=200, body={"data": response})
    
    def __validate_inputs(self, user_id: any, new_balance: any) -> None:
        try:
            if not isinstance(user_id, int):
                raise HttpBadRequestError("user_id must be an integer")
                
            if not isinstance(new_balance, (int, float)):
                raise HttpBadRequestError("new_balance must be a number")
                
            if new_balance < 0:
                raise HttpBadRequestError("new_balance cannot be negative")
                
        except HttpBadRequestError as error:
            raise HttpBadRequestError('Invalid inputs') from error