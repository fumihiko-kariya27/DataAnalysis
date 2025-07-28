import json

from django.views import View
from django.template.response import TemplateResponse

from ecSiteAnalysis.usecase.PurchaseAnalysis import PurchaseAnalysis

class PurchaseView(View):
    action = ...;
    
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs);
        return view;
    
    def __init__(self, **kwargs):
        self._action = kwargs.pop("action", None);
        self._service = PurchaseAnalysis();
        super().__init__(**kwargs);
        
    
    def get(self, request, *args, **kwargs):
        from_day = request.GET.get("from_day");
        to_day = request.GET.get("to_day")
        if self._action == "show":
            # 全期間の購入明細の取得
            purchase_detail = self._service.get_purchase(from_day, to_day);
            context = {
                "purchase_detail": purchase_detail,    
            }
            return TemplateResponse(request, "purchase/summary_list.html", context);
        elif self._action == "monthly_sales":
            # 月間、商品毎の購入合計の取得
            sales_monthly = self._service.get_monthly_sales(from_day, to_day);
            months = sorted(set(month for month, item in sales_monthly.keys()));
            items = sorted(set(item for month, item in sales_monthly.keys()));
            month_value = [];
            for item in items:
                summary = {
                    "item": item,
                    "month_value": [sales_monthly.get((month, item), 0) for month in months],
                }
                month_value.append(summary);
            context = {
                "month_list": months,
                "sales_monthly": month_value,
            }
            return TemplateResponse(request, "purchase/sales/monthly.html", context);
        