from ecSiteAnalysis.infrastructure.customer.repository.CustomerRepositoryImpl import CustomerRepositoryImpl

class CustomerAnalysis:
    
    def __init__(self):
        self._repository = CustomerRepositoryImpl();
    
    
    def get_all(self) -> list:
        return self._repository.get_all();