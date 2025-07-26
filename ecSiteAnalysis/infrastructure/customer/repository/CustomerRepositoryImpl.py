from ecSiteAnalysis.domain.customer.CustomerRepository import CustomerRepository
from ecSiteAnalysis.infrastructure.customer.repository.CustomerModel import CustomerModel

class CustomerRepositoryImpl(CustomerRepository):
    
    def __init__(self):
        self._model = CustomerModel;