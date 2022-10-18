
def miles_to_yards(miles):
    yards_in_mile = 1760
    return miles * yards_in_mile


def yards_to_miles(yards):
    yards_in_mile = 1760
    # round to 16 places to match example
    return round((yards / yards_in_mile), 16)


def yards_to_feet(yards):
    feet_in_yard = 3
    return round((yards * feet_in_yard), 16)


def feet_to_yards(feet):
    feet_in_yard = 3
    return round((feet / feet_in_yard), 16)


def feet_to_inches(feet):
    inches_in_foot = 12
    return round((feet * inches_in_foot), 16)


def inches_to_feet(inches):
    inches_in_foot = 12
    return round((inches / inches_in_foot), 16)