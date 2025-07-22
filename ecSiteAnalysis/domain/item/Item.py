class Item:
    
    def __init__(self, id: str, name: str, price: int):
        self._id = id;
        self._name = name;
        self._price = price;
    
    
    def get_id(self):
        return self._id;
    
    
    def get_name(self):
        return self._name;
    
    
    def get_price(self):
        return self._price;