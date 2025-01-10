class HttpBadRequestError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
        self.status_code = 400
        self.error_type = "bad_request"