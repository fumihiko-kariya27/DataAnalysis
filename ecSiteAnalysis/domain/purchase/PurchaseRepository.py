from abc import ABC, abstractmethod
from datetime import date

from ecSiteAnalysis.domain.purchase.PurchaseSummary import PurchaseSummary

class PurchaseRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> list[PurchaseSummary]:
        pass;
    
    
    @abstractmethod
    def get_payment_date_from(self, from_day: date) -> list[PurchaseSummary]:
        pass;
    
    
    @abstractmethod
    def get_payment_date_to(self, to_day: date) -> list[PurchaseSummary]:
        pass;
    
    
    @abstractmethod
    def get_payment_date_between(self, from_day: date, to_day: date) -> list[PurchaseSummary]:
        pass;