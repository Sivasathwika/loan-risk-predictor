import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("cleaned_loan_data.csv")
print("Data loaded:",df.shape)

#plot1
plt.figure(figsize=(8,5))
sns.countplot(x="loan_status",data=df)
plt.title("Loan Default Distribution")
plt.xlabel("Loan Status (0=No Default, 1=Default)")
plt.ylabel("Number of people")
plt.savefig("loan_staus_chart.png")
print("Chart saved as loan_status_chart.png")

#plot2
plt.figure(figsize=(8,5))
sns.histplot(df["person_age"], bins=20)
plt.title("Age Distribution of Loan Applicants")
plt.xlabel("Age")
plt.ylabel("count")
plt.savefig("age_distribution.png")
print("Age chart saved")

#plot3- lOan amount by defaukt values
plt.figure(figsize=(8,5))
sns.boxplot(x="loan_status", y="loan_amnt", data=df)
plt.title("Loan Amount by Default Status")
plt.xlabel("Loan Status (0=No Default, 1=Default)")
plt.ylabel("Loan Amount")
plt.savefig("loan_amount_boxplot.png")
print("Loan amount chart saved")

#plot4 - Correlation  heatmap
plt.figure(figsize=(8,5))
numeric_df=df.select_dtypes(include=['float64','int64'])
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
print("Heatmap saved")