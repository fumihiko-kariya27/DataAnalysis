from datetime import date

from django.db.models import Prefetch

from ecSiteAnalysis.domain.purchase.PurchaseRepository import PurchaseRepository
from ecSiteAnalysis.domain.purchase.PurchaseSummary import PurchaseSummary
from ecSiteAnalysis.domain.item.Item import Item;
from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseSummaryModel import PurchaseSummaryModel
from ecSiteAnalysis.infrastructure.purchase.repository.PurchaseDetailModel import PurchaseDetailModel

class PurchaseRepositoryImpl(PurchaseRepository):
    
    def get_payment_date_between(self, from_day: date, to_day: date) -> list[PurchaseSummary]:
        query_set = PurchaseSummaryModel.objects.prefetch_related(
            Prefetch(
                "purchasedetailmodel_set",
                queryset = PurchaseDetailModel.objects.select_related("item_id")
            )
        ).filter(payment_datetime__gte=from_day, payment_datetime__lte=to_day);
        
        return [self._to_domain_object(row) for row in query_set];
    
    
    def _to_domain_object(self, model: PurchaseSummaryModel) -> PurchaseSummary:
        name = model.customer_id.name if model.customer_id else "unknown";
        payment_datetime = model.payment_datetime;
        details = model.purchasedetailmodel_set.all();
        detail = details[0];
        item_model = detail.item_id;
        item = Item(item_model.id, item_model.name, item_model.price);
        quantity = detail.quantity;
        return PurchaseSummary(name, payment_datetime, item, quantity);