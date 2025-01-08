from abc import ABC, abstractmethod

class RegisterUserControllerInterface(ABC):
    @abstractmethod
    def register_user(self, username: str, password: str) -> dict:
        pass
