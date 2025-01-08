from abc import ABC, abstractmethod

class LoginUserControllerInterface(ABC):
    @abstractmethod
    def login_user(self, username: str, password: str) -> dict:
        pass
