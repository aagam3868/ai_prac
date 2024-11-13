import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(r'C:\Users\LENOVO\Desktop\C C++\AI_PRACTICAL\merged_data.csv')

# Display the shape of the data
print("Shape of the DataFrame:", df.shape)

# Handle missing values (NaN) by showing count of NaN in each column
nan_count = df.isnull().sum()
print("\nCount of NaN values in each column:\n", nan_count)

# Select only numeric columns for mean and covariance
numeric_df = df.select_dtypes(include=[np.number])

# Mean of the numeric columns
mean_values = numeric_df.mean()
print("\nMean of numeric columns:\n", mean_values)

# Covariance matrix for numeric columns
covariance_matrix = numeric_df.cov()
print("\nCovariance matrix:\n", covariance_matrix)
