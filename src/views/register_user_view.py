from src.controllers.interfaces.register_user_controller_interface import RegisterUserControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class RegisterUserView(ViewInterface):
    def __init__(self, register_user_controller: RegisterUserControllerInterface) -> None:
        self.register_user_controller = register_user_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body['username']
        password = http_request.body['password']
        self.__validate_inputs(username, password)
        response = self.register_user_controller.register_user(username, password)
        return HttpResponse(status_code=201, body={"data": response})
    
    def __validate_inputs(self, username: any, password: any) -> None:
        if (
            not username 
            or not password 
            or not isinstance(username, str) 
            or not isinstance(password, str)
        ): raise Exception('Invalid inputs')
