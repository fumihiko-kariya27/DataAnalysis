from ecSiteAnalysis.domain.customer.CustomerRepository import CustomerRepository
from ecSiteAnalysis.infrastructure.customer.repository.CustomerModel import CustomerModel

class CustomerRepositoryImpl(CustomerRepository):
    
    def __init__(self):
        self._model = CustomerModel
    
    
    def get_all(self) -> list:
        customers = self._model.objects.all();
        ret = [];
        for customer in customers:
            ret.append(customer.to_domain_object());
        return ret;