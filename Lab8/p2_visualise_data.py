import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'car_data.csv'

# read csv, drop extra index col:
df = pd.read_csv(filename).drop(['Unnamed: 0'],axis=1)

print(df)