from django.db import models

class ItemModel(models.Model):
    
    class Meta:
        db_table = "item_master";
        indexes = [
            models.Index(fields=["name"])
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=0), name="constraint_item_price_greater_than_zero"),
        ];
        
    
    id = models.CharField(max_length=4, primary_key=True, verbose_name="商品ID");
    name = models.CharField(max_length=10, verbose_name="商品名");
    price = models.IntegerField(verbose_name="価格");
    
    def __str__(self):
        return self.name;