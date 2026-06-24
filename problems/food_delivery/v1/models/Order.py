from abc import ABC, abstractmethod


class Order(ABC):
    next_order_id = 0

    def __init__(self):
        self.__user = None
        self.__restaurant = None
        self.__items = []
        self.__payment_strategy = None
        self.__total = 0.0
        self.__scheduled = ""

        Order.next_order_id += 1
        self.__order_id = Order.next_order_id

    def __del__(self):
        self.__payment_strategy = None

    def process_payment(self):
        if self.__payment_strategy:
            self.__payment_strategy.pay(self.__total)
            return True
        else:
            print("Please choose a payment mode first")
            return False

    @abstractmethod
    def get_type(self):
        pass

    # Getters
    def get_order_id(self):
        return self.__order_id

    def get_user(self):
        return self.__user

    def get_restaurant(self):
        return self.__restaurant

    def get_items(self):
        return self.__items

    def get_scheduled(self):
        return self.__scheduled

    def get_total(self):
        return self.__total

    # Setters
    def set_user(self, user):
        self.__user = user

    def set_restaurant(self, restaurant):
        self.__restaurant = restaurant

    def set_items(self, items):
        self.__items = items
        self.__total = 0

        for item in items:
            self.__total += item.get_price()

    def set_payment_strategy(self, payment_strategy):
        self.__payment_strategy = payment_strategy

    def set_scheduled(self, scheduled):
        self.__scheduled = scheduled

    def set_total(self, total):
        self.__total = total