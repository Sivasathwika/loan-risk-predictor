import pandas as pd

df=pd.read_csv("credit_risk_dataset.csv")

print("Shape of dataset:",df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
print("\nBasic Statistics:")
print(df.describe())

print("\nLoan Status distribution:")
print(df["loan_status"].value_counts())

print("\nLoan Intent types:")
print(df["loan_intent"].value_counts())

print("\nHome Ownership types:")
print(df["person_home_ownership"].value_counts())

print("\nMissing values in each column:")
print(df.isnull().sum())




