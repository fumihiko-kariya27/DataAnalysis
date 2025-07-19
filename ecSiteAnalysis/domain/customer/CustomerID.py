import re

class CustomerID:
    
    # 顧客IDは先頭がアルファベット２文字、続けて数字6桁が続くものを正とする
    _id_format = re.compile("[A-Z]{2}[0-9]{6}");
    
    def __init__(self, id: str):
        if CustomerID._id_format.fullmatch(id) is None:
            raise ValueError(f"顧客IDのフォーマットが不正です: ID={id}")
        self._id = id;


    def __eq__(self, other):
        if isinstance(other, CustomerID):
            return self._id == other.get_id();
        return NotImplemented;
    
    
    def get_id(self):
        return self._id;