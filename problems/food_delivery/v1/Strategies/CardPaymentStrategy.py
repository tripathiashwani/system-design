from abc import ABC, abstractmethod
from .PaymentStrategy import PaymentStrategy
class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self, card):
        self.__card_number = card

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card ({self.__card_number})")