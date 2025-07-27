from django.views import View
from django.template.response import TemplateResponse

from ecSiteAnalysis.usecase.PurchaseAnalysis import PurchaseAnalysis

class PurchaseView(View):
    
    def __init__(self):
        self._service = PurchaseAnalysis();
        
    
    def get(self, request, *args, **kwargs):
        from_day = request.GET.get("from_day");
        to_day = request.GET.get("to_day")
        purchase_detail = self._service.get_purchase(from_day, to_day);
        context = {
            "purchase_detail": purchase_detail,    
        }
        return TemplateResponse(request, "customer/purchase_detail.html", context);