from functools import reduce


def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


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


def inches_to_cm(inches):
    cm_in_inch = 2.54
    return round((inches * cm_in_inch), 16)


def cm_to_inches(inches):
    cm_in_inch = 2.54
    return round((inches / cm_in_inch), 16)


def cm_to_meters(cm):
    cm_in_meter = 100
    return round((cm / cm_in_meter), 16)


def meters_to_cm(cm):
    cm_in_meter = 100
    return round((cm * cm_in_meter), 16)


def meters_to_km(meters):
    meter_in_km = 1000
    return round((meters / meter_in_km), 16)


def km_to_meters(km):
    meter_in_km = 1000
    return round((km * meter_in_km), 16)


def km_to_au(km):
    km_in_au = 149597870.700
    answer = km / km_in_au
    print("Answer: {:.24f}".format(answer))
    return answer


def au_to_km(au):
    km_in_au = 149597870.700
    return round((au * km_in_au), 16)


def au_to_ly(ly):
    ly_to_au = 63241.07708426628026865358
    return round((ly / ly_to_au), 24)


def ly_to_au(ly):
    ly_to_au = 63241.07708426628026865358
    return round((ly * ly_to_au), 16)

# ================================ Extra Credit ================================


def cm_to_mm(cm):
    mm_in_cm = 10
    return round((cm * mm_in_cm), 16)


def mm_to_cm(mm):
    mm_in_cm = 10
    return round((mm / mm_in_cm), 16)


def mm_to_micrometer(mm):
    micrometers_in_mm = 1000
    return round((mm * micrometers_in_mm), 16)


def micrometer_to_mm(mm):
    micrometers_in_mm = 1000
    return round((mm / micrometers_in_mm), 16)


def micrometer_to_angstrom(micrometer):
    angstroms_in_micrometer = 10000
    return round((micrometer * angstroms_in_micrometer), 16)


def angstrom_to_micrometer(angstrom):
    angstroms_in_micrometer = 10000
    return round((angstrom / angstroms_in_micrometer), 16)
