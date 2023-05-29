import pandas as pd
import numpy as np
from scipy.optimize import minimize
from sklearn.preprocessing import StandardScaler

def calculate_weights(data_file):

    df = pd.read_csv(data_file)

    scaler = StandardScaler()
    cols_to_scale = ['normalized_smoking', 'normalized_copd', 'normalized_covid', 'normalized_drowning', 'normalized_sepsis', 'normalized_flu', 'normalized_pneumonia', 'normalized_vaccination', 'vals']
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    df['normalized_vaccination'] = 1 - df['normalized_vaccination']

    def objective(weights, df):
        if weights[1] < 0.1:
          weights[1] = 0.1
        weighted_sum = (
            df['normalized_smoking'] * weights[0]
            + df['normalized_copd'] * weights[1]
            + df['normalized_covid'] * weights[2]
            + df['normalized_drowning'] * weights[3]
            + df['normalized_sepsis'] * weights[4]
            + df['normalized_flu'] * weights[5]
            + df['normalized_pneumonia'] * weights[6]
            + df['normalized_vaccination'] * weights[7]
        )
        return np.sum((weighted_sum - df['vals']) ** 2)

    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    initial_weights = [1 / 8, 1/8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8, 1 / 8]

    result = minimize(objective, initial_weights, args=(df), method='SLSQP', constraints=cons)

    return result.x