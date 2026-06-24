from .Order import Order

class DeliveryOrder(Order):
    def __init__(self):
        super().__init__()
        self.__user_address = ""

    def get_type(self):
        return "Delivery"

    # Getter
    def get_user_address(self):
        return self.__user_address

    # Setter
    def set_user_address(self, address):
        self.__user_address = address