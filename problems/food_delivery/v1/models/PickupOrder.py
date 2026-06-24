from .Order import Order

class PickupOrder(Order):
    def __init__(self):
        super().__init__()
        self.__restaurant_address = ""

    def get_type(self):
        return "Pickup"

    # Getter
    def get_restaurant_address(self):
        return self.__restaurant_address

    # Setter
    def set_restaurant_address(self, address):
        self.__restaurant_address = address