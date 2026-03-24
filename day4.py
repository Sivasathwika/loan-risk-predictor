import pandas as pd

df=pd.read_csv("credit_risk_dataset.csv")

print("Original shape:",df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

#filling missing interest rates with median
median_rate=df["loan_int_rate"].median()
print("Median interest rate:",median_rate)
df["loan_int_rate"]=df["loan_int_rate"].fillna(median_rate)

#filling missing employment length with median
median_emp=df["person_emp_length"].median()
print("Median employment length:",median_emp)
df["person_emp_length"]=df["person_emp_length"].fillna(median_emp)


print("\nMissing values after filling:")
print(df.isnull().sum())

#fixing impossible ages
print("\nAge distriution before cleaning:")
print(df["person_age"].describe())

#removing rows where age is above 100
df=df[df["person_age"]<=100]

print("\nAge distribution after cleaning:")
print(df["person_age"].describe())
print("\nNew Shape:",df.shape)


df.to_csv("cleaned_loan_data.csv",index=False)
print("\nCleaned dataset saved as cleaned_loan_data.csv")
print("Final Shape:",df.shape)
