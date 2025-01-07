from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def register_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def edit_balance(self, id: int, balance: float) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, id: int) -> tuple[int, str, float]:
        pass

