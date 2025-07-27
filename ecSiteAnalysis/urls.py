from django.urls import path

from ecSiteAnalysis.presentation.CustomerView import CustomerListView
from ecSiteAnalysis.presentation.PurchaseView import PurchaseView


app_name = "ecSiteAnalysis"

urlpatterns = [
    path("all/", CustomerListView.as_view(), name="customer_all"),
    path("purchase", PurchaseView.as_view(), name="purchase_view"),
]