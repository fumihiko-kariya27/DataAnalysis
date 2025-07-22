from django.urls import path

from ecSiteAnalysis.presentation.CustomerView import CustomerListView
from ecSiteAnalysis.presentation.PurchaseView import PurchaseView


app_name = "ecSiteAnalysis"

urlpatterns = [
    path("all/", CustomerListView.as_view(), name="customer_all"),
    path("purchase_between", PurchaseView.as_view(), name="purchase_between_view"),
]