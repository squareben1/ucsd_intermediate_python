import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./all_alpha_19.csv', header='infer')

df2 = df.query('Stnd == "T3B125" and (Fuel == "Gasoline" | Fuel == "Diesel")')

# print(df2.head(99))

cols = ['Model', 'Displ', 'Fuel', 'City MPG',
        'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']

new_df = df2[cols].reset_index(drop=True)

float_cols = ['City MPG', 'Hwy MPG', 'Cmb MPG']

print(new_df.dtypes)


for i in float_cols:
    new_df[i] = new_df[i].astype(float)

print(new_df.dtypes)


# 'Model'  Car manufacturer and model
# 'Displ'  Engine displacement (size of engine)
# 'Fuel'  Type of fuel
# 'City MPG'  Number of miles the car gets per gallon of fuel in the city
# 'Hwy MPG'  Number of miles the car gets per gallon of fuel on the highway
# 'Cmb MPG' Combined number of miles the car gets per gallon of fuel in the city and
# highway
# 'Greenhouse Gas Score'  Calculated score indicating the car’s efficiency (higher is
# better)
