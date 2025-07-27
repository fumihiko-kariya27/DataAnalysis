from datetime import date

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

from ecSiteAnalysis.domain.purchase.PurchaseSummary import PurchaseSummary
from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseRepositoryImpl import PurchaseRepositoryImpl

class PurchaseAnalysis:
    
    def __init__(self):
        self._repository = PurchaseRepositoryImpl();
    
    
    def get_purchase(self, from_day: date, to_day: date) -> list[PurchaseSummary]:
        """購入日が指定期間内の購入明細を取得する

        Parameters
        ----------
        from_day : date
            取り込み開始日
        to_day : date
            取り込み終了日

        Returns
        -------
        list[PurchaseSummary]
            購入日が指定期間内の購入明細一覧

        """
        purchases = [];
        if from_day is not None and to_day is not None:
            # 開始日及び終了日がいずれも指定されている場合は購入日が指定期間内の明細を取得する
            purchases = self._repository.get_payment_date_between(from_day, to_day);
        elif from_day is not None and to_day is None:
            # 開始日のみ指定されている場合は購入日が開始日以降の明細を取得する
            purchases = self._repository.get_payment_date_from(from_day);
        elif from_day is None and to_day is not None:
            # 終了日のみ指定されている場合は購入日が終了日以前の明細を取得する
            purchases = self._repository.get_payment_date_to(to_day);
        else:
            # 開始日も終了日も指定されていない場合は全期間の購入明細を取得する
            purchases = self._repository.get_all();
        
        df_purchase = pd.DataFrame([purchase.to_dict() for purchase in purchases]);
        if is_datetime64_any_dtype(df_purchase["payment_datetime"]):
            df_purchase["payment_datetime"] = pd.to_datetime(df_purchase["payment_datetime"]);
        df_purchase["payment_month"] = df_purchase["payment_datetime"].dt.strftime("%Y%m");
        return purchases;
        
        
        