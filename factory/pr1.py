from abc import ABC,abstractmethod
d={}
class Notification(ABC):
    @abstractmethod
    def send(self,msg):
        pass

class EmailNotification(Notification):
    def send(self,msg):
        return f'message: {msg} sent through Email'
class SmsNotification(Notification):
    def send(self,msg):
        return f'message: {msg} sent through SMS'
class WhatsaapNotification(Notification):
    def send(self,msg):
        return f'message: {msg} sent through Whatsaap'

class NotificatioinFactory(ABC):
    @abstractmethod
    def create(self):
        pass

class EmailNotificationFactory(NotificatioinFactory):
    def create(self):
        return EmailNotification()
class WhatsaapNotificationFactory(NotificatioinFactory):
    def create(self):
        return WhatsaapNotification()
class SmsNotificationFactory(NotificatioinFactory):
    def create(self):
        return SmsNotification()

class OrderService():
    def __init__(self,factory,msg):
        self.factory=factory
        self.msg=msg
    def send_notification(self):
        obj = self.factory.create()
        return obj.send(self.msg)
    
d['email']=EmailNotificationFactory()
d['whatsaap']=WhatsaapNotificationFactory()
d['sms']=SmsNotificationFactory()

# s={'email','sms','whatsaap'}
fac=input(f'enter the type from the list:{d.keys()}')
a=OrderService(d[fac],'this is pavan ....')
print(a.send_notification())
