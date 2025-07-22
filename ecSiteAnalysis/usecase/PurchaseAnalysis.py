from datetime import date

from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseRepositoryImpl import PurchaseRepositoryImpl

class PurchaseAnalysis:
    
    def __init__(self):
        self._repository = PurchaseRepositoryImpl();
    
    
    def get_payment_date_between(self, from_day: date, to_day: date) -> list:
        return self._repository.get_payment_date_between(from_day, to_day);