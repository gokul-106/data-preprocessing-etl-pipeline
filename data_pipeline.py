import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)
def preprocess_data(df):
    num_features = df.select_dtypes(include=['int64', 'float64']).columns
    cat_features = df.select_dtypes(include=['object']).columns
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])
    full_pipeline = ColumnTransformer([
        ('num', num_pipeline, num_features),
        ('cat', cat_pipeline, cat_features)
    ])
    transformed_data = full_pipeline.fit_transform(df)
    transformed_df = pd.DataFrame(
        transformed_data, 
        columns=num_features.tolist() + list(full_pipeline.named_transformers_['cat'].named_steps['encoder'].get_feature_names_out(cat_features))
    )
    
    return transformed_df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file ="raw_data.csv"
    output_file = "processed_data.csv"

    print("Loading data...")
    data = load_data(input_file)
    
    print("Processing data...")
    processed_data = preprocess_data(data)
    
    print("Saving processed data...")
    save_data(processed_data, output_file)
    

    print("ETL Pipeline Completed Successfully!")
