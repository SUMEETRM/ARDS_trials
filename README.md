# ARDS_trials
<span style="color: red; font-weight: bold;">[Click to Watch Video](https://drive.google.com/file/d/1WJQOWu0SnG4v_dCVGX8ohOGCxHOdfnQ1/view?usp=sharing)</span>

<!-- Project Logo -->
<p align="center">
  <a href="https://ibb.co/WcsTvzR"><img src="https://i.ibb.co/RC75T6J/Screenshot-2023-05-14-at-8-13-29-PM.png" alt="Screenshot-2023-05-14-at-8-13-29-PM" border="0"></a>
</p>

<!-- Project Title -->
<h1 align="center">ARDS Clinical Trials</h1>

<!-- Project Description -->
<p align="center">
  Comprehensive analysis and visualizatio of ARDS (Acute Respiratory Distress Syndrome) clinical trial loacations across the USA.
</p>

<!-- Table of Contents -->
## Table of Contents
- [Data Sources](#data-sources)
- [Folium](#folium)
- [Supervised Learning for Weights](#supervised-learning-for-weights)
- [Repository Structure](#repository-structure)
- [Documentation](#documentation)

<!-- Data Sources -->
## :file_folder: Data Sources

The `ards_data` folder in this repository hosts several key datasets that are instrumental for our analysis on Acute Respiratory Distress Syndrome (ARDS) and associated factors. 

Here is a breakdown of the datasets included:

- :hospital: `ARDS_centers`: Contains names and geographic coordinates of hospitals known for their specialization in ARDS treatment. Data is originally sourced from [ClinicalTrials.gov](https://clinicaltrials.gov/ct2/results?cond=ARDS&map_cntry=US&draw=2&rank=1#rowId0).

- :chart_with_upwards_trend: `County_COPD_prevalence`: A dataset from the CDC that provides information about the prevalence of Chronic Obstructive Pulmonary Disease (COPD) at a county level.

- :swimmer: `Drowning_data`: A dataset providing insights into drowning incidents, sourced from the CDC.

- :sneezing_face: `flu_data`: This dataset contains data on flu cases, as provided by the CDC.

- :face_with_thermometer: `Pnem`: Includes data related to pneumonia cases, also sourced from the CDC.

- :mask: `Covid_nyt`: Contains detailed COVID-19 case data, sourced from the [New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html).

- :ambulance: `Sepsis1`: CDC-sourced dataset containing detailed case data on sepsis.

- :syringe: `Vaccination`: Includes data related to flu vaccination rates.

- :map: `uscounties`: A comprehensive dataset containing details about US county coordinates, population figures, and FIPS codes.

- :smoking: `Tobacco`: A dataset that provides insights into tobacco usage rates.

- :us: `States.csv`: A dataset containing the names, abbreviations, and central coordinates of US states.

Refer to the original data sources for more comprehensive details and context about these datasets.



<!-- Folium -->
## Folium
The project leverages Folium, a Python library for creating interactive maps, to visualize the geographical distribution of clinical trial locations. The interactive maps provide a comprehensive overview of the trial sites and their distribution across different regions.

<!-- Supervised Learning for Weights -->
## :open_file_folder: Supervised Learning for Weights

This folder contains a Python script that utilizes supervised learning to calculate optimal weights for various risk factors in our Acute Respiratory Distress Syndrome (ARDS) study. 

The algorithm applies a constrained optimization approach to find the best-suited weights that minimize the discrepancy between the weighted sum of risk factors and the actual ARDS mortality rates. 

:arrow_down_small: Here is a brief overview of the key steps in the script:

1. Import required libraries (Pandas, Numpy, Scipy, and Sklearn)
2. Load the dataset 'state_data_1.csv'
3. Normalize the risk factors and mortality rates using `StandardScaler` from Sklearn
4. Define the objective function for optimization. This function calculates the weighted sum of normalized risk factors and returns the sum of squared errors between this weighted sum and the actual mortality rates
5. Set a constraint for the optimization problem to ensure that the sum of weights equals 1
6. Define initial weights as equal fractions (1/8 in this case)
7. Run the optimization algorithm (Sequential Least Squares Programming, or 'SLSQP') with the objective function, initial weights, and constraints
8. Print the optimal weights obtained from the optimization



<!-- Repository Structure -->
## :open_file_folder: Repository Structure

This repository is structured in a way that makes the analysis flow intuitive and easy to follow. Here's a quick tour:

- :notebook: `ards_map.ipynb`: This is the primary Jupyter notebook where all the magic happens. It integrates various components of the project and generates a detailed heatmap in HTML format. The code in this notebook is modular, making it easy to reuse and adapt to your needs.

- :balance_scale: `weight_optimization.py`: This Python script contains an optimization algorithm that calculates the best-suited weights for generating the weighted Folium heatmap. The weights are derived from a supervised learning algorithm optimized against an ARDS mortality study.

- :globe_with_meridians: `usa_map.html`: This is a ready-to-use HTML map showcasing 500 clinical trial locations in a heatmap format. It's a direct product of running the `ards_map.ipynb` notebook.

- :gear: `dataloader.py`: This Python script is responsible for loading all the necessary data from the `ards_data` folder.

- :file_folder: `ards_data`: This folder is the data repository hosting several datasets used in the analysis. For a more detailed description of the individual datasets, please refer to the [Data Sources](#data-sources) section.

- :bookmark_tabs: `ards_state_vals`: This file contains state-wise ARDS mortality rates, as derived from a linked study.

- :page_facing_up: `ARDS_locations.csv`: This CSV file offers comprehensive data on various studies, including details such as the number of participants, participant age and sex, study dates, and updates on study completion.

Explore each of these components to get a better understanding of the project



<!-- Documentation -->
## Documentation
For more detailed information about the project, data sources, methodologies, and findings, please refer to the [project documentation](docs/).

Feel free to explore the repository and utilize the provided resources for your research and analysis.

<!-- Acknowledgements -->
## Acknowledgements
Special thanks to the contributors and collaborators who have made this project possible.

<!-- License -->
## License
This project is licensed under the [MIT License](LICENSE).


