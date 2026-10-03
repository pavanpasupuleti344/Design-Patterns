from abc import ABC,abstractmethod
class Weather:
    def __init__(self,temp=None,sub=None):
        self.subscribers=[]
        self.add_subscribers(sub)
        self.temp=temp 
    def add_subscribers(self,obj):
        if obj is None:return
        if isinstance(obj,list):
            self.subscribers.extend(obj)
        else:
            self.subscribers.append(obj)
    def remove_subscribers(self,obj):
        if isinstance(obj,list):
            for i in obj:
                if i in self.subscribers:
                    self.subscribers.remove(i)
        else:
            if obj in self.subscribers:
                self.subscribers.remove(obj)
        
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self,new):
        self._temp=new
        for sub in self.subscribers:
            print(sub.send(self.temp))
    


class Notification(ABC):
    @abstractmethod
    def send(self,temp):
        # return f'the temperature is :{self.temp} MobileApp'
        pass
class MobileApp(Notification):
    def send(self,temp):
        return f'the temperature is :{temp} MobileApp'
class WebApp(Notification):
    def send(self,temp):
        return f'the temperature is :{temp} WebApp'
class SmartWatch(Notification):
    def send(self,temp):
        return f'the temperature is :{temp} SmartWatch'


m,w,sw=MobileApp(),WebApp(),SmartWatch()
w=Weather(90,[m,w,sw])
# w.add_subscribers([MobileApp(),WebApp(),SmartWatch()])
w.remove_subscribers([m,sw])

w.temp=900