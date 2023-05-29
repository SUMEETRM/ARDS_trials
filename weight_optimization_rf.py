import numpy as np
from scipy.optimize import minimize
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def calculate_weights_rf(data_file):
    #This data file will be state_data_1.csv
    #Need to return a list with the weights
    # Load the data
    df = pd.read_csv(data_file)

    # Apply Standardization (Z-score normalization)
    # Normalize both axes
    scaler = StandardScaler()
    cols_to_scale = ['normalized_smoking', 'normalized_copd', 'normalized_covid', 'normalized_drowning', 'normalized_sepsis', 'normalized_flu', 'normalized_pneumonia', 'normalized_vaccination', 'vals']
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    # Modify the 'normalized_vaccination' column since greater vaccination rates imply lower rates of ARDS according to studies
    df['normalized_vaccination'] = 1 - df['normalized_vaccination']

    # Define features and target
    from sklearn.ensemble import RandomForestRegressor

    features = df[cols_to_scale[:-1]]  # Excludes 'vals'
    target = df['vals']

    # Fit the Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42) 
    # The number of trees in the forest (n_estimators) can be adjusted
    model.fit(features, target)

    # Predict the target for the features
    predictions = model.predict(features)

    # Calculate the R-squared score
    r2 = r2_score(target, predictions)
    importances = model.feature_importances_
    return importances, r2
    #print("R-squared: ", r2)

