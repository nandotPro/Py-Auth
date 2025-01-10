class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
        self.status_code = 422
        self.error_type = "unprocessable_entity"