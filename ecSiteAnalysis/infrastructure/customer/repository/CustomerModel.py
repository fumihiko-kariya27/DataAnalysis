from django.db import models

from ecSiteAnalysis.domain.customer import Customer, CustomerID
from ecSiteAnalysis.infrastructure.prefecture.repository.PrefectureModel import PrefectureModel

class CustomerModel(models.Model):
    
    class Meta:
        db_table = "customer_master"
        constraints = [
            models.CheckConstraint(check=models.Q(age__gt=0), name="constraint_age_greater_than_zero"),
            models.CheckConstraint(check=models.Q(age__lte=100), name="constraint_age_less_than_or_equal_100")
        ]
    
    id = models.CharField(max_length=8, primary_key=True, verbose_name="顧客ID")
    name = models.CharField(max_length=10, verbose_name="氏名")
    registration_datetime = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")
    kana = models.CharField(max_length=20, verbose_name="氏名カナ")
    email = models.EmailField(verbose_name="メールアドレス")
    sex = models.CharField(max_length=1, verbose_name="性別")
    age = models.IntegerField(verbose_name="年齢")
    birthday = models.DateField(verbose_name="誕生日")
    prefecture = models.ForeignKey(PrefectureModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="都道府県")
    
    def __str__(self):
        return self.name
    
    
    def to_domain_object(self):
        return Customer.Customer(CustomerID.CustomerID(self.id), self.name, self.registration_datetime, self.sex, self.age, self.prefecture);
