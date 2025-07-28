from django.urls import path

from ecSiteAnalysis.presentation.CustomerView import CustomerListView
from ecSiteAnalysis.presentation.PurchaseView import PurchaseView


app_name = "ecSiteAnalysis"

urlpatterns = [
    path("all/", CustomerListView.as_view(), name="customer_all"),
    path("purchase", PurchaseView.as_view(action="show"), name="purchase_show"),
    path("purchase/sales/monthly", PurchaseView.as_view(action="monthly_sales"), name="purchase_monthly_sales"),
]