from abc import ABC, abstractmethod
from typing import Dict, Type, List

class Subscriber(ABC):

    def __init__(self):
        self.message=""

    @abstractmethod
    def update(self,message:str):
        pass
    
    

class Email(Subscriber):

    def update(self,text:str):
        print(f"message achieved on email :{text}")
        self.message=text



class SMS(Subscriber):

    def update(self,text:str):
        print(f"message achieved on SMS :{text}")
        self.message=text

class Publisher:

    def __init__(self,lst:List[Subscriber]):
        self.subscribers=lst

    def notify(self,text:str):
        for s in self.subscribers:
            s.update(text)

    def publish(self,text:str):
        self.notify(text)

    def subscribe(self,subscriber:Subscriber):
        self.subscribers.append(subscriber)


class SubscriberFactory:

    _registry: Dict[str, Type[Subscriber]] = {
        "email": Email,
        "sms": SMS,
    }

    def create(self,type:str):
        if type not in self._registry:
            raise ValueError(f"Unsupported payment method: {type}")

        return self._registry[type]()
    

if __name__ == "__main__":
    factory:SubscriberFactory=SubscriberFactory()
    
    email_subs:Subscriber=factory.create("email")
    sms_subs:Subscriber=factory.create("sms")
    publisher:Publisher=Publisher([email_subs,sms_subs])
    publisher.publish("hey guys")
    print(f"Email subs text :{email_subs.message}")
    print(f"SMS subs text :{sms_subs.message}")


         
        


