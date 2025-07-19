from django.db import models

class PrefectureModel(models.Model):
    
    class Meta:
        db_table = "prefecture_master"
        indexes = [
            models.Index(fields=["name"])
        ]
    
    name = models.CharField(max_length=4, primary_key=True, verbose_name="県名")
    region = models.CharField(max_length=3, verbose_name="地域")
    
    def __str__(self):
        return self.name