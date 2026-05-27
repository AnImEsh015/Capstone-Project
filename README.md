# Real Estate Price Prediction & Analysis: Gurgaon Properties

## 📌 Project Overview
This capstone project involves an end-to-end Data Science and Machine Learning workflow to analyze and predict real estate property prices in Gurgaon. The project processes data for both apartments (flats) and independent houses, exploring various factors that influence property valuations.

## 📊 Dataset
The dataset contains real estate listings with attributes such as location, property type, price, area, coordinates, and other key features. The raw data includes files like `flats.csv`, `Independent_houses.csv`, and `gurgaon_properties.csv`, which were subsequently merged and refined throughout the pipeline.

## 🚀 Project Workflow
This repository contains multiple Jupyter Notebooks that logically break down the machine learning lifecycle:

1. **Data Collection & Cleaning**
   - `Data_cleaning(Flats).ipynb` & `data_cleaning_houses.ipynb`: Initial cleaning of raw property data.
   - `merge-flat--houses.ipynb`: Consolidating flats and independent houses into a unified dataset.
   
2. **Data Preprocessing & Handling**
   - `Missing_value_imputation.ipynb`: Strategies to handle null or missing values.
   - `Outlier_Detection.ipynb`: Identifying and treating extreme anomalies in property prices and sizes.
   - `data_preprocessing_v2.ipynb`: Finalizing the dataset structure for analysis.

3. **Exploratory Data Analysis (EDA)**
   - `Eda-univariate_analysis.ipynb`: Analyzing individual variables to understand their distributions.
   - `EDA_Multivartiate_analysis.ipynb`: Exploring relationships between multiple variables (e.g., price vs. location, area vs. price).
   - `Data_visualization.ipynb`: Visual representations of market trends.

4. **Feature Engineering & Selection**
   - `feature_engineerng.ipynb`: Creating new meaningful features (like price per sqft or adding geographical coordinates).
   - `Feature_selction.ipynb`: Selecting the most relevant variables to improve model accuracy and reduce dimensionality.

5. **Machine Learning & Modeling**
   - `Baseline Model.ipynb`: Establishing a basic model to benchmark performance.
   - `Model_selection.ipynb`: Training and comparing various machine learning algorithms to find the best-performing model for price prediction.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3
* **Environment:** Jupyter Notebook
* **Libraries:** * *Data Manipulation:* Pandas, NumPy
  * *Data Visualization:* Matplotlib, Seaborn
  * *Machine Learning:* Scikit-Learn

## 📁 Repository Structure
```text
📦 Capstone-Project
 ┣ 📜 Baseline Model.ipynb
 ┣ 📜 Data_cleaning(Flats).ipynb
 ┣ 📜 data_cleaning_houses.ipynb
 ┣ 📜 Missing_value_imputation.ipynb
 ┣ 📜 Outlier_Detection.ipynb
 ┣ 📜 Eda-univariate_analysis.ipynb
 ┣ 📜 EDA_Multivartiate_analysis.ipynb
 ┣ 📜 Feature_selction.ipynb
 ┣ 📜 feature_engineerng.ipynb
 ┣ 📜 Model_selection.ipynb
 ┣ 📜 merge-flat--houses.ipynb
 ┣ 📜 flats.csv / Independent_houses.csv
 ┣ 📜 gurgaon_properties_cleaned_v2.csv
 ┗ 📜 README.md
