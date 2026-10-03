from abc import ABC,abstractmethod
class Shipping(ABC):
    @abstractmethod
    def fee(self):
        pass
class NormalShipping(Shipping):
    def fee(self):
        return 50
class ExpressShipping(Shipping):
    def fee(self):
        return 120
class FreeShipping(Shipping):
    def fee(self):
        return 0
class Order:
    def __init__(self,amount,type=NormalShipping()):
        self.amount=amount
        self.type=type
    def set_startegy(self,change):
        self.type=change
    def check_out(self):
        return f'the order price: {self.amount}\ndelivery charge:{self.type.fee()}\nTotal:{self.amount+self.type.fee()}\n'
            
o1=Order(150,ExpressShipping())
print(o1.check_out())
o1.set_startegy(FreeShipping())
print(o1.check_out())
