# Intermediate Python Course - UCSD

## Lab 3

As instructed, all code is in one .py file; `src/restaraunt.py`. 

It became apparent that making classes from strings with multiple words in them would be a pain using `getattr(sys.modules[__name__], food_cls_name)`. Since accounting for this wasn't explicitly stated I decided not to spend time on this. It could have been with some string manipulation to capitalize letters before stripping spaces. 

### How to Run

`cd` into project directory and run: `export PYTHONPATH="$PWD"`

To run any [program]:

`python3 [program]`

e.g.

`python3 src/restaraunt.py`

### Output of program

Note: I left the new class prints in. 

    Creating new instance pf Restaurant
    Creating new instance of Food class
    Cheeseburger: grill all-beef patty
    Cheeseburger: flip patty
    Cheeseburger: put cheese on patty
    Cheeseburger: put patty on bun and add toppings
    Cheeseburger: All done!
    Cheeseburger: 5.99
    Creating new instance of Food class
    Pasta: boiling water
    Pasta: saute onions, garlic and tomatoes for sauce.
    Pasta: put pasta in water
    Pasta: season the sauce
    Pasta: plate pasta and add sauce on top
    Pasta: All done!
    Pasta: 8.99
    Sorry, this restaurant does not make: mac and cheese module '__main__' has no attribute 'Mac and cheese'
    This restaurant had 2 orders today for a total of 14.98 in sales
    Using existing instance.
    This restaurant had 2 orders today for a total of 14.98 in sales