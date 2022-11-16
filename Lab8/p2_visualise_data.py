import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'car_data.csv'

# Load the “car_data.csv” file: 5pts
# drop extra index col:
df = pd.read_csv(filename, header='infer', index_col=0)


# First plot: 10pts
scatter_plot = df.plot.scatter(x='Displ', y='City MPG', c='r')


# Prepare color/size lists for second plot: 15pts

def get_fuel_colour(fuel_type):
    if fuel_type == 'Gasoline':
        return 'r'
    elif fuel_type == 'Diesel':
        return 'g'


c = [get_fuel_colour(x) for x in df['Fuel']]
s = [8 * x for x in df['Greenhouse Gas Score']]


# Second plot: 10pts

compelling_plot = df.plot.scatter(x='Displ', y='City MPG', s=s, c=c, alpha=0.5)

# Extra Credit: Legend and axes labels: 3pts (?)
plt.title('City Driving: MPG vs. Displacement')
plt.xlabel('Displacement')
plt.ylabel('City Miles Per Gallon')

plt.legend()

# NOTE: I could not get the legend to show the labels despite trying for longer than I should have.
# It drove me slightly mad. I tried setting the x and y labels inline in the plot.scatter definition
# as well as here as well several of other ways. Decided to let this bit of extra credit go for the
# sake of my sanity.
# If you can shed any light on why this wouldn't work it would be appreciated.

# Extra Credit - New chart: 7pts
fig = plt.figure()
ax = plt.axes()

ax.plot(df['City MPG'], label='City MPG')
ax.plot(df['Hwy MPG'], label='Hwy MPG')

plt.title('City Driving vs Highway Driving')
plt.xlabel('Records')
plt.ylabel('MPG')

plt.legend()

plt.show()
