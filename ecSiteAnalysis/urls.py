from django.urls import path

from ecSiteAnalysis.presentation.CustomerView import CustomerListView
from ecSiteAnalysis.presentation.PurchaseView import PurchaseBetweenView


app_name = "ecSiteAnalysis"

urlpatterns = [
    path("all/", CustomerListView.as_view(), name="customer_all"),
    path("purchase_between", PurchaseBetweenView.as_view(), name="purchase_between_view"),
]