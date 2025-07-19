from datetime import datetime
from . import CustomerID

class Customer:
    
    def __init__(self, id: CustomerID, name: str, registration_datetime: datetime, sex: str, age: int, pref: str):
        self._id = id;
        self._name = name;
        self._registration_datetime = registration_datetime;
        self._sex = sex;
        self._age = age;
        self._pref = pref;
    
    
    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.getId() == other.get_id();
        return NotImplemented;
    
    
    def __str__(self):
        return f"ID:{self._id.get_id()}、 氏名：{self._name}"
    
    
    def get_id(self):
        return self._id.get_id();
    

    def get_name(self):
        return self._name;
    
    
    def get_registration_datetime(self):
        return self._registration_datetime.strftime("%Y年%m月%d日");
    
    
    def get_sex(self):
        return self._sex;
    
    
    def get_age(self):
        return self._age;
    
    
    def get_pref(self):
        return self._pref;