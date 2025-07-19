from abc import ABC, abstractmethod

class CustomerRepository(ABC):
    
    @abstractmethod
    def get_all() -> list:
        # 顧客一覧を取得する
        pass