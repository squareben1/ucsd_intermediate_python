import sys

class Restaraunt():

    _orders = 0
    _total_sales = 0

    def __new__(cls, *args, **kwargs):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            print("Creating new instance")
            cls.instance = super(Restaraunt, cls).__new__(cls, *args, **kwargs)
        else:
            print("Using existing instance.")
        return cls.instance

    def __str__(self):
        return f"Total orders = {self._orders}, totalling {self._total_sales} in sales."

    def order_food(self, food_type):
        # call the static order_food method of the Food class, 
        # passing it food_type as its only argument.
        # Additionally, this is where you will have to alter the _orders and 
        # _total_sales variables if you are going down that route

        # order_food(): wrapper call to Food.order_food()
        pass


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
                

                new_class = getattr(sys.modules[__name__], food_cls_name)
                new_class = new_class()
                print(new_class.prepare())
                # globalVars = vars()
                # globalVars[food_cls_name]
        except Exception as E:
            print("Exception: ", E)


class Cheeseburger(Restaraunt):
    def price(self):
        return 1

    def prepare(self):
        # In derived classes, this method acts as a façade that encapsulates 
        # the complex process for making this specific food
        return "Preparing cheeseburger"

# rest1 = Restaraunt()
# rest2 = Restaraunt()


# print(rest1)
# rest2._orders = 1
# print(rest2)
# print(rest1)

# cheeseburger = Food()

Food.order_food("cheeseburger")