from datetime import datetime
import uuid


class Expense:
    def __init__(self,amount,category,description=""):
        self.id=str(uuid.uuid4())
        self.amount=amount
        self.category=category
        self.description=description
        self.created_at=datetime.now().isoformat()



    def to_dict(self):
        return{
            "id":self.id,
            "amount":self.amount,
            "category":self.category,
            "description":self.description,
        }


    @classmethod
    def from_dict(cls,data):
        obj=cls(
            amount=data.get("amount",""),
            category=data.get("category",""),
            description=data.get("description",""),
        )
        

        obj.id=data.get("id") 
        obj.created_at=data.get("created_at")

        return obj
    