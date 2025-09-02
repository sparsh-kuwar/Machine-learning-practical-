import pandas as pd 
df = pd.read_csv('realistic_linear_regression_dataset.csv')
print(df.head())  # Display the first few rows of the dataset
print(df.describe())  # Display summary statistics of the dataset
print(df.info())  # Display information about the dataset, including data types and non-null counts
print(df.isnull().sum())  # Check for missing values in the dataset