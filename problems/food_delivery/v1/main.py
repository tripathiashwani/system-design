from pathlib import Path
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from v1.TomatoApp import TomatoApp
from v1.models.User import User
from v1.Strategies.UpiPayment import UpiPaymentStrategy

def main():
    # Create TomatoApp object
    tomato = TomatoApp()

    # Simulate user coming in
    user = User(101, "Aditya", "Delhi")
    print(f"User: {user.get_name()} is active.")

    # User searches restaurants by location
    restaurant_list = tomato.search_restaurants("Delhi")

    if not restaurant_list:
        print("No restaurants found!")
        return

    print("Found Restaurants:")
    for restaurant in restaurant_list:
        print(f" - {restaurant.get_name()}")

    # User selects restaurant
    tomato.select_restaurant(user, restaurant_list[0])
    print(f"Selected restaurant: {restaurant_list[0].get_name()}")

    # User adds items to cart
    tomato.add_to_cart(user, "P1")
    tomato.add_to_cart(user, "P2")

    tomato.print_user_cart(user)

    # User checkout
    order = tomato.checkout_now(
        user,
        "Delivery",
        UpiPaymentStrategy("1234567890")
    )

    # User pays
    tomato.pay_for_order(user, order)


if __name__ == "__main__":
    main()