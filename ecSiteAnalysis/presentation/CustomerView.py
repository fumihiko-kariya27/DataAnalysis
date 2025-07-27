from django.views import View

from ecSiteAnalysis.usecase.CustomerAnalysis import CustomerAnalysis

class CustomerListView(View):
    
    def __init__(self):
        self._customer_service = CustomerAnalysis()
    
    
    def get(self, request, *args, **kwargs):
        pass;
    