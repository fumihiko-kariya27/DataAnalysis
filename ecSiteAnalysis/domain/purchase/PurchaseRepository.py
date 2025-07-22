from abc import ABC, abstractmethod
from datetime import date

class PurchaseRepository(ABC):
    
    @abstractmethod
    def get_payment_date_between(self, from_day: date, to_day: date) -> list:
        pass;