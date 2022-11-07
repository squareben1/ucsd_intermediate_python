import sys
from time import sleep

class Restaurant():

    _orders = 0
    _total_sales = 0

    def __new__(cls, *args, **kwargs):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""

        if not hasattr(cls, 'instance'):
            print("Creating new instance")
            cls.instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
        else:
            print("Using existing instance.")
        return cls.instance

    def __str__(self):
        return f"This restaurant had {self._orders} today for a total of {self._total_sales} in sales"

    def order_food(self, food_type):
        # call the static order_food method of the Food class,
        # passing it food_type as its only argument.
        # Additionally, this is where you will have to alter the _orders and
        # _total_sales variables if you are going down that route

        # order_food(): wrapper call to Food.order_food()
        food = Food.order_food(food_type)
        if food:
            food.prepare()
            self._orders += 1
            self._total_sales += food.price()
        return food


class Food():
    def __init__(self):
        print("Creating new instance of Food class")
        pass

    def price(self):
        return 0

    def prepare(self):
        # In derived classes, this method acts as a façade that encapsulates
        # the complex process for making this specific food
        pass

    @staticmethod
    def order_food(food_type):

        try:
            if type(food_type) == str:
                food_type = food_type.lower().strip()
                food_cls_name = food_type.capitalize()

                food_class = getattr(sys.modules[__name__], food_cls_name)
                food = food_class()
                # print(food_class.prepare())
                return food

        except Exception as E:
            print(f"Sorry, this restaurant does not make: {food_type}", E)


class Cheeseburger(Food):
    price_usd = 5.99

    def price(self):
        return self.price_usd

    def prepare(self):
        print(f"{__class__.__name__}: Flippin' that Krabby patty.")
        sleep(2)

    def __str__(self):
        return f"{__class__.__name__}: {self.price()}"


class Pasta(Food):
    price_usd = 4.99

    def price(self):
        return self.price_usd

    def prepare(self):
        print(f"{__class__.__name__}: Boiling water.")
        sleep(2)

    def __str__(self):
        return f"{__class__.__name__}: {self.price()}"



def main():
    r = Restaurant()
    food = r.order_food("cheeseburger")
    if food:
        print(food)
    food = r.order_food("pasta")
    if food:
        print(food)
    food = r.order_food("mac and cheese") # doesn't exist, prints failure message
    if food:
        print(food)
    print(r) # If you did extra credit, it will show number of orders and total sales
    # Use this test to prove we have a single instance of Restaurant:
    r2 = Restaurant()
    print(r2)

if __name__ == "__main__":
    main()

# rest1 = Restaurant()
# rest2 = Restaurant()


# print(rest1)
# rest2._orders = 1
# print(rest2)
# print(rest1)

# cheeseburger = Food()

# burger = Food.order_food("cheeseburger")
# burger2 = Food.order_food("cheeseburger")
# print(burger)
# print(burger2.prepare())
