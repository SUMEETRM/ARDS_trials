import pandas as pd

#Note: These values are the ones that are optimized against
#Source: https://www.sciencedirect.com/science/article/pii/S0012369220349370
#Trends and Geographic Variation in Acute Respiratory Failure and ARDS Mortality in the United States

#To view this data allocated state wise, go to ards_map.py -> state_data()
vals = [4.7, 2.0, 3.0, 2.7, 3.4, 2.5, 3.8, 2.7, 2.9, 2.7, 2.1, 2.9, 2.0, 2.5, 3.6, 3.3, 3.0, 2.8, 2.4, 2.5, 2.9, 3.6, 2.8, 2.2, 2.6, 2.6, 2.4, 3.1, 1.9, 2.9, 4.5, 3.2, 3.1, 3.3, 3.1, 1.3, 4.2, 2.1, 3.5, 3.1, 2.5, 1, 2.3, 3.6, 3.7, 2.7, 2.1]

df_vals = pd.DataFrame(vals, columns=['vals'])

df_vals.to_csv('vals.csv', index=False)
