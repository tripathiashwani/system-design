class Cart:
    def __init__(self):
        self.__restaurant = None
        self.__items = []

    def get_restaurant(self):
        return self.__restaurant

    def set_restaurant(self, restaurant):
        self.__restaurant = restaurant

    def add_item(self, item):
        self.__items.append(item)

    def get_items(self):
        return self.__items

    def get_total_cost(self):
        return sum(item.get_price() for item in self.__items)

    def is_empty(self):
        return len(self.__items) == 0

    def clear(self):
        self.__restaurant = None
        self.__items.clear()