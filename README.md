Data Preprocessing ETL Pipeline
A production-style data preprocessing pipeline designed to automate data cleaning and transformation for machine learning models.
Project Overview
This project implements an ETL-inspired workflow that prepares raw datasets for modeling by handling missing values, scaling numerical features, and encoding categorical variables.
Key Features
- Built modular preprocessing functions for reusable workflows.
- Implemented Scikit-learn Pipelines for numerical and categorical transformations.
- Automated missing value imputation using statistical strategies.
- Applied StandardScaler for feature normalization.
- Used OneHotEncoder to convert categorical data into model-ready format.
- Generated a fully processed dataset ready for machine learning.
Tech Stack
Python, Pandas, NumPy, Scikit-learn
Business Value
Improves data quality and consistency while reducing manual preprocessing effort, enabling faster and more reliable machine learning development.
How to Run
1. Provide the raw dataset  
2. Execute the pipeline script  
3. Retrieve the processed dataset for downstream ML tasks
