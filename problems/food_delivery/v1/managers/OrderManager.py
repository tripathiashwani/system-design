class OrderManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__orders = []
        return cls.__instance

    def add_order(self, order):
        self.__orders.append(order)

    def list_orders(self):
        print("\n--- All Orders ---")

        for order in self.__orders:
            print(
                f"{order.get_type()} order for {order.get_user().get_name()} "
                f"| Total: ₹{order.get_total()} "
                f"| At: {order.get_scheduled()}"
            )