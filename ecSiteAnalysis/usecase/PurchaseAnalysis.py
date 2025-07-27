from datetime import date

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

from ecSiteAnalysis.domain.purchase.PurchaseSummary import PurchaseSummary
from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseRepositoryImpl import PurchaseRepositoryImpl

class PurchaseAnalysis:
    
    def __init__(self):
        self._repository = PurchaseRepositoryImpl();
    
    
    def get_all(self) -> list[PurchaseSummary]:
        df_purchase = pd.DataFrame([purchase.to_dict() for purchase in self._repository.get_all()]);
        if is_datetime64_any_dtype(df_purchase["payment_datetime"]):
            df_purchase["payment_datetime"] = pd.to_datetime(df_purchase["payment_datetime"]);
        
        df_purchase["payment_month"] = df_purchase["payment_datetime"].dt.strftime("%Y%m");
        return self._repository.get_all();
    
    
    def get_payment_date_between(self, from_day: date, to_day: date) -> list[PurchaseSummary]:
        df_purchase = pd.DataFrame([purchase.to_dict() for purchase in self._repository.get_payment_date_between(from_day, to_day)]);
        if is_datetime64_any_dtype(df_purchase["payment_datetime"]):
            df_purchase["payment_datetime"] = pd.to_datetime(df_purchase["payment_datetime"]);
        
        df_purchase["payment_month"] = df_purchase["payment_datetime"].dt.strftime("%Y%m");
        
        return self._repository.get_payment_date_between(from_day, to_day);