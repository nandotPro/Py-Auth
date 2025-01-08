from src.controllers.interfaces.login_user_controller_interface import LoginUserControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class LoginUserView(ViewInterface):
    def __init__(self, login_user_controller: LoginUserControllerInterface) -> None:
        self.login_user_controller = login_user_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body['username']
        password = http_request.body['password']
        self.__validate_inputs(username, password)
        response = self.login_user_controller.login_user(username, password)
        return HttpResponse(status_code=200, body={"data": response})
    
    def __validate_inputs(self, username: any, password: any) -> None:
        if (
            not username 
            or not password 
            or not isinstance(username, str) 
            or not isinstance(password, str)
        ): raise Exception('Invalid inputs')
