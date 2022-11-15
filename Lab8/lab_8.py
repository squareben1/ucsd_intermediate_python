import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the “all_alpha_19.csv” file: 5pts
df = pd.read_csv('./all_alpha_19.csv', header='infer')

# Filter the results: 15pts
df2 = df.query('Stnd == "T3B125" and (Fuel == "Gasoline" | Fuel == "Diesel")')


# Migrate to new DataFrame with smaller column list: 10pts
cols = ['Model', 'Displ', 'Fuel', 'City MPG',
        'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']

new_df = df2[cols].reset_index(drop=True)

float_cols = ['City MPG', 'Hwy MPG', 'Cmb MPG']

print("Types before conversion: ", new_df.dtypes)

# Convert MPG columns to float: 5pts
for i in float_cols:
    new_df[i] = new_df[i].astype(float)

print("Types after conversion: ", new_df.dtypes)


def mpg_to_kml(mpg):
    """Convert miles per gallon to km per liter."""
    kml = 0.42514
    return mpg * kml


print("BEFORE: ")
print(new_df)

new_df = new_df.assign(CityKML=mpg_to_kml(new_df['City MPG']))
new_df = new_df.assign(HwyKML=mpg_to_kml(new_df['Hwy MPG']))
new_df = new_df.assign(CmbKML=mpg_to_kml(new_df['Cmb MPG']))

print("AFTER: ")
print(new_df)


# 'Model'  Car manufacturer and model
# 'Displ'  Engine displacement (size of engine)
# 'Fuel'  Type of fuel
# 'City MPG'  Number of miles the car gets per gallon of fuel in the city
# 'Hwy MPG'  Number of miles the car gets per gallon of fuel on the highway
# 'Cmb MPG' Combined number of miles the car gets per gallon of fuel in the city and
# highway
# 'Greenhouse Gas Score'  Calculated score indicating the cars efficiency (higher is
# better)
