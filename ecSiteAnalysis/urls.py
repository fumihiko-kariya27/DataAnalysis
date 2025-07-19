from django.urls import path

from ecSiteAnalysis.presentation.CustomerView import CustomerView


app_name = "ecSiteAnalysis"

urlpatterns = [
    path("all/", CustomerView.as_view(), name="customer_all")
]