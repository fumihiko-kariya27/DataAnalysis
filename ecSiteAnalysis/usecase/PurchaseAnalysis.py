from datetime import date

import pandas as pd

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
        return purchases;
    
    
    def get_monthly_sales(self, from_day: date, to_day: date) -> dict[tuple[str, str], int]:
        """指定取り込み期間内の購入明細から、月間売上を算出する
        集約単位は月単位/商品単位で売上を計算したデータが返却される

        Parameters
        ----------
        from_day : date
            取り込み開始日
        to_day : date
            取り込み終了日

        Returns
        -------
        dict[tuple[str, str], int]
            取り込み期間内の月毎・商品毎の売上データ
            辞書のkeyであるtupleの第一要素に月名、第二要素に商品名、valueに合計金額が設定される
        """
        purchase_detail = self.get_purchase(from_day, to_day);
        df_purchase = pd.DataFrame([purchase.to_dict() for purchase in purchase_detail]);
        df_purchase["payment_month"] = df_purchase["payment_datetime"].dt.strftime("%Y/%m");
        group_by_monthly = df_purchase.groupby(["payment_month", "item_name"])["item_price"].sum();
        return group_by_monthly.to_dict();
        
        
        
        