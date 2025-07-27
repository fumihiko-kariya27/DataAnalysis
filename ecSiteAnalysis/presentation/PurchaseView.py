from django.views import View
from django.utils.dateparse import parse_date
from django.template.response import TemplateResponse

from ecSiteAnalysis.usecase.PurchaseAnalysis import PurchaseAnalysis

class PurchaseView(View):
    
    def __init__(self):
        self._service = PurchaseAnalysis();
        
    
    def get(self, request, *args, **kwargs):
        if request.GET.get("from_day") is not None and request.GET.get("to_day") is not None:
            return self._get_between(request, args, kwargs)
        else:
            return self._get_all(request, args, kwargs);
    
    
    def _get_all(self, request, *args, **kwargs):
        purchase_detail = self._service.get_all();
        context = {
            "purchase_detail": purchase_detail,    
        }
        return TemplateResponse(request, "customer/purchase_detail.html", context);
    
    
    def _get_between(self, request, *args, **kwargs):
        from_day_str = request.GET.get("from_day");
        from_day = parse_date(from_day_str);
        
        to_day_str = request.GET.get("to_day");
        to_day = parse_date(to_day_str);
        
        if (from_day > to_day):
            # 取得期間の日付の前後関係が正しくない場合、処理を異常終了する
            raise ValueError(f"取得開始日時は${from_day}は取得終了日時${to_day}よりも過去の日付である必要があります");
        
        purchase_detail = self._service.get_payment_date_between(from_day, to_day);
        context = {
            "purchase_detail": purchase_detail,
        }
        return TemplateResponse(request, "customer/purchase_detail.html", context);