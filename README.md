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
  Comprehensive analysis and insights on ARDS (Acute Respiratory Distress Syndrome) clinical trials.
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
## Supervised Learning for Weights
To optimize the weightings of various factors in the analysis, supervised learning techniques are employed. The model learns from the historical data to assign appropriate weights to different variables, enabling more accurate predictions and insights.

<!-- Repository Structure -->
## Repository Structure
The repository is organized as follows:
├── data/ # Processed and cleaned datasets used for analysis
├── notebooks/ # Jupyter notebooks with detailed code and analysis
├── scripts/ # Utility scripts for data preprocessing and visualization
├── results/ # Output files, reports, and visualizations generated from the analysis


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


