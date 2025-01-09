class HttpRequest:
    def __init__(
            self, 
            body: dict = None, 
            headers: dict = None, 
            params: dict = None,
            token_data: dict = None
        ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_data = token_data
