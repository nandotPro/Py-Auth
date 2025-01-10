class HttpNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
        self.status_code = 404
        self.error_type = "not_found"