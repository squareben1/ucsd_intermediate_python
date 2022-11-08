import sys
from time import sleep


class Restaurant():

    _orders = 0
    _total_sales = 0

    def __new__(cls, *args, **kwargs):
        """Create singleton object, if no instance exists,
        else returns the previous singleton object"""

        if not hasattr(cls, 'instance'):
            print("Creating new instance pf Restaurant")
            cls.instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
        else:
            print("Using existing instance.")
        return cls.instance

    def __str__(self):
        """Class string method."""
        return f"This restaurant had {self._orders} orders today for a total of ${self._total_sales} in sales"

    def order_food(self, food_type):
        """Call static order_food method of Food class and alter vars."""
        food = Food.order_food(food_type)

        if food:
            self._orders += 1
            self._total_sales += food.price()
        return food


class Food():
    def __init__(self):
        print("Creating new instance of Food class")
        pass

    def price(self):
        """Placeholder for child class to return price."""
        return 0

    def prepare(self):
        """Façade that encapsulates the complex process for 
        making the specific food of derived class."""
        pass

    @staticmethod
    def order_food(food_type):
        """Create instance class from food_type string"""
        try:
            if type(food_type) == str:
                food_type = food_type.lower().strip()
                food_cls_name = food_type.capitalize()
                food_class = getattr(sys.modules[__name__], food_cls_name)

                food = food_class()
                food.prepare()

                return food

        except Exception as E:
            print(f"Sorry, this restaurant does not make: {food_type}", E)


class Cheeseburger(Food):
    price_usd = 5.99

    def price(self):
        """Return price of food item."""
        return self.price_usd

    def prepare(self):
        """Prepare food item."""
        print(f"{__class__.__name__}: grill all-beef patty")
        print(f"{__class__.__name__}: flip patty")
        print(f"{__class__.__name__}: put cheese on patty")
        print(f"{__class__.__name__}: put patty on bun and add toppings")
        print(f"{__class__.__name__}: All done!")

        sleep(2)

    def __str__(self):
        """Class string method."""
        return f"{__class__.__name__}: {self.price()}"


class Pasta(Food):
    price_usd = 8.99

    def price(self):
        """Return price of food item."""
        return self.price_usd

    def prepare(self):
        """Prepare food item."""
        print(f"{__class__.__name__}: boiling water")
        print(f"{__class__.__name__}: saute onions, garlic and tomatoes for sauce.")
        print(f"{__class__.__name__}: put pasta in water")
        print(f"{__class__.__name__}: season the sauce")
        print(f"{__class__.__name__}: plate pasta and add sauce on top")
        print(f"{__class__.__name__}: All done!")

        sleep(2)

    def __str__(self):
        """Class string method."""
        return f"{__class__.__name__}: {self.price()}"

# Extra Credit


class Sushi(Food):
    price_usd = 10.99

    def price(self):
        """Return price of food item."""
        return self.price_usd

    def prepare(self):
        """Prepare food item."""
        print(f"{__class__.__name__}: cook rice")
        print(f"{__class__.__name__}: slice fish")
        print(f"{__class__.__name__}: don't cook fish")
        print(f"{__class__.__name__}: place fish on rice")
        print(f"{__class__.__name__}: All done!")

        sleep(2)

    def __str__(self):
        """Class string method."""
        return f"{__class__.__name__}: {self.price()}"


def main():
    r = Restaurant()
    food = r.order_food("cheeseburger")
    if food:
        print(food)
    food = r.order_food("pasta")
    if food:
        print(food)
    # doesn't exist, prints failure message
    food = r.order_food("mac and cheese")
    if food:
        print(food)
    # Extra credit, uncomment to test:
    # food = r.order_food("sushi")
    # if food:
    #     print(food)
    print(r)  # If you did extra credit, it will show number of orders and total sales
    # Use this test to prove we have a single instance of Restaurant:
    r2 = Restaurant()
    print(r2)


if __name__ == "__main__":
    main()
