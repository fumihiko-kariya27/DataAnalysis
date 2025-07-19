from django.views import View
from django.template.response import TemplateResponse

from ecSiteAnalysis.usecase.CustomerAnalysis import CustomerAnalysis

class CustomerView(View):
    
    def __init__(self):
        self._customer_service = CustomerAnalysis()
    
    
    def get(self, request, *args, **kwargs):
        all_customers = self._customer_service.get_all();
        context = {
            "customers": all_customers    
        }
        return TemplateResponse(request, 'customer/list.html', context);