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
