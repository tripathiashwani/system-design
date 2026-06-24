from abc import ABC, abstractmethod
from .PaymentStrategy import PaymentStrategy
class UpiPaymentStrategy(PaymentStrategy):
    def __init__(self, __mobile_no):
        self.__mobile_no = __mobile_no

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI ({self.__mobile_no})")