class RestaurantManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__restaurants = []
        return cls.__instance

    def add_restaurant(self, restaurant):
        self.__restaurants.append(restaurant)

    def search_by_location(self, location):
        result = []
        location = location.lower()

        for restaurant in self.__restaurants:
            restaurant_location = restaurant.get_location().lower()
            if restaurant_location == location:
                result.append(restaurant)

        return result