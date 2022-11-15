import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./all_alpha_19.csv', header='infer')

df2 = df.query('Stnd == "T3B125" and (Fuel == "Gasoline" | Fuel == "Diesel")')

print(df2.head(99))
