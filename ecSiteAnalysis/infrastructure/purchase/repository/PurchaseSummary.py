from django.db import models

from ecSiteAnalysis.infrastructure.customer.repository.CustomerModel import CustomerModel

class PurchaseSummaryModel(models.Model):
    
    class Meta:
        db_table = "purchase_summary"
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=0), name="constraint_price_greater_than_zero"),
        ];
    
    
    id = models.CharField(max_length=11, primary_key=True, verbose_name="ID");
    price = models.IntegerField(verbose_name="購入金額");
    payment_datetime = models.DateTimeField(verbose_name="購入日時");
    customer_id = models.ForeignKey(CustomerModel, null=True, on_delete=models.SET_NULL, verbose_name="顧客ID");