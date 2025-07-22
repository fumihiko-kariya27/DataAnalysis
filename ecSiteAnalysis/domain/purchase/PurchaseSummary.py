from datetime import datetime

from ecSiteAnalysis.domain.item.Item import Item

class PurchaseSummary:
    
    def __init__(self, name: str, payment_datetime: datetime, item: Item, quantity: int):
        self._name = name;
        self._payment_datetime = payment_datetime;
        self._item = item;
        self._quantity = quantity;
    
    
    def get_total_price(self) -> int:
        return self._price * self._quantity;
    
    
    def get_name(self) -> str:
        return self._name;
    
    
    def get_payment_date(self) -> str:
        return self._payment_datetime.strftime("%Y/%m/%d")
    
    
    def get_item_name(self) -> str:
        return self._item.get_name() if self._item is not None else "不明な商品です";
    
    
    def get_item_price(self) -> int:
        return self._item.get_price() if self._item is not None else 0;
    
    
    def get_quantity(self) -> int:
        return self._quantity;