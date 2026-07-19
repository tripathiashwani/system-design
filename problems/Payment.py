from abc import ABC, abstractmethod
import threading
from typing import Dict, Type

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

class CreditCardPayment(Payment):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Credit Card."


class PayPalPayment(Payment):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using PayPal."


class PaymentGateway:

    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, paymentmethod:Payment):
        if not self._initialized:
            self.paymentmethod=paymentmethod

class PaymentProcessor:

    def __init__(self):
        self.paymentgateway=PaymentGateway()
    

    
    def pay(self, payment_method: Payment, amount: int) -> None:
        # retries / logging / metrics could live here
        payment_method.pay(amount)




class PaymentFactory:
    """
    Registry-based factory (OCP compliant)
    """
    _registry: Dict[str, Type[Payment]] = {
        "creditcard": CreditCardPayment,
        "paypal": PayPalPayment,
    }

    @classmethod
    def create(cls, method: str, *, balance: int, rate: float) -> Payment:
        if method not in cls._registry:
            raise ValueError(f"Unsupported payment method: {method}")

        return cls._registry[method](balance, rate)
if __name__ == "__main__":
    amount =input("what amount you want to pay?")
    method=input("what method would you go for?")

    payment_factory=PaymentFactory()
    payment_method=payment_factory.create(method)

    payment_processor:PaymentProcessor=PaymentProcessor()
    payment_processor.pay(payment_method,amount)




        
        
        
        