class Restaurant:
    next_restaurant_id = 0   # static variable

    def __init__(self, name: str, location: str):
        self.__name = name
        self.__location = location
        Restaurant.next_restaurant_id += 1
        self.__restaurant_id = Restaurant.next_restaurant_id
        self.__menu = []

    def __del__(self):
        print(f"Destroying Restaurant: {self.__name}, and clearing its menu.")
        self.__menu.clear()

    # Getters
    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_restaurant_id(self):
        return self.__restaurant_id

    def get_menu(self):
        return self.__menu

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_location(self, location):
        self.__location = location

    # Menu methods
    def add_menu_item(self, item):
        self.__menu.append(item)