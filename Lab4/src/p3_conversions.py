
def miles_to_yards(miles):
    yards_in_mile = 1760
    return miles * yards_in_mile


def yards_to_miles(yards):
    yards_in_mile = 1760
    # round to 16 places to match example
    return round((yards / yards_in_mile), 16)


def yards_to_feet(yards):
    feet_in_yard = 3
    # round to 16 places to match example
    return round((yards * feet_in_yard), 16)


def feet_to_yards(yards):
    feet_in_yard = 3
    # round to 16 places to match example
    return round((yards / feet_in_yard), 16)