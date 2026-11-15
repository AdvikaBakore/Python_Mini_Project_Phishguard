import pandas as pd

# Load the dataset
df = pd.read_csv("phishing_features.csv")

# Look at the first few rows
print(df.head())

# How many rows and columns?
print("Shape:", df.shape)

# What are the column names?
print("Columns:", df.columns.tolist())

# How many phishing vs legitimate examples?
print(df['label'].value_counts())