import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'car_data.csv'

# read csv, drop extra index col:
df = pd.read_csv(filename, header='infer', index_col=0)

print(df)

scatter_plot = df.plot.scatter(x='Displ', y='City MPG', c='r')

# plt.show()

def get_fuel_colour(fuel_type):
    if fuel_type == 'Gasoline':
        return 'r'
    elif fuel_type == 'Diesel':
        return 'g'

c = [get_fuel_colour(x) for x in df['Fuel']]
s = [8 * x for x in df['Greenhouse Gas Score']]

print(s)
compelling_plot = df.plot.scatter(x='Displ', y='City MPG', s=s, c=c, alpha=0.5)

plt.show()
