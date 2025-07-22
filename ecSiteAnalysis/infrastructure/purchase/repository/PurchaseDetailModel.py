from django.db import models

from ecSiteAnalysis.infrastructure.item.repository.ItemModel import ItemModel
from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseSummaryModel import PurchaseSummaryModel

class PurchaseDetailModel(models.Model):
    
    class Meta:
        db_table = "purchase_detail";
        constraints = [
            models.CheckConstraint(check=models.Q(quantity__gt=0), name="constraint_wuantity_greater_than_zero"),
        ];
    
    id = models.IntegerField(primary_key=True, verbose_name="購入詳細ID");
    purchase_summary_id = models.ForeignKey(PurchaseSummaryModel, on_delete=models.CASCADE, verbose_name="購入明細ID");
    item_id = models.ForeignKey(ItemModel, null=True, on_delete=models.SET_NULL, verbose_name="購入商品ID");
    quantity = models.IntegerField(verbose_name="数量");