from datetime import date

import pandas as pd

from ecSiteAnalysis.domain.purchase.PurchaseSummary import PurchaseSummary
from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseRepositoryImpl import PurchaseRepositoryImpl

class PurchaseAnalysis:
    
    def __init__(self):
        self._repository = PurchaseRepositoryImpl();
    
    
    def get_payment_date_between(self, from_day: date, to_day: date) -> list[PurchaseSummary]:
        df_purchase = pd.DataFrame([purchase.to_dict() for purchase in self._repository.get_payment_date_between(from_day, to_day)]);
        print(df_purchase.describe());
        return self._repository.get_payment_date_between(from_day, to_day);