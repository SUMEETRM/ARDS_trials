import pandas as pd

def load_data():
    county_coordinates = pd.read_csv('ards_data/uscounties.csv')
    smoking_data = pd.read_csv('ards_data/tob.csv')
    copd_data = pd.read_csv('ards_data/County_COPD_prevalence.csv')
    covid_data = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-2023.csv')
    sepsis_data = pd.read_csv('ards_data/sepsis1.csv')
    drowning_data = pd.read_csv('ards_data/Drowning_Data.csv')
    vaccination_data = pd.read_csv('ards_data/vaccination.csv')
    flu_data = pd.read_csv('ards_data/flu_data.csv')
    pneumonia_data = pd.read_csv('ards_data/pnem.csv')
    ards_centers = pd.read_csv('ards_data/ARDS_centers.csv')

    return county_coordinates, smoking_data, copd_data, covid_data, sepsis_data, drowning_data, vaccination_data, flu_data, pneumonia_data, ards_centers
