import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'car_data.csv'

# read csv, drop extra index col:
df = pd.read_csv(filename, header='infer', index_col=0)

print(df)

scatter_plot = df.plot.scatter(x='Displ', y='City MPG', c='r')

plt.show()