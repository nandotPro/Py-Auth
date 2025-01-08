from abc import ABC, abstractmethod

class EditBalanceControllerInterface(ABC):
    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float) -> dict:
        pass
