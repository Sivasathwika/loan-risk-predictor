import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

#Load cleaned data
df=pd.read_csv("cleaned_loan_data.csv")
print("Data Loaded:",df.shape)

#check column types
print("\nColumn types:")
print(df.dtypes)

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

#Encode text columns
text_columns=["person_home_ownership","loan_intent","loan_grade","cb_person_default_on_file"]

for column in text_columns:
    df[column]=le.fit_transform(df[column])

print("\nAfter encoding:")
print(df.dtypes)
print("\nSample of encoded data:")
print(df.head())

#Split features and target
X=df.drop("loan_status",axis=1)
y=df["loan_status"]

print("Features shape:",X.shape)
print("Target shape:",y.shape)

#split into train and test 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

print("\nTraininng set size:", X_train.shape)
print("Testing set size:", X_test.shape)

#Train Logistic Regression Model
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
print("Model trained successfully")

#Make predictions
y_pred=model.predict(X_test)

#Evaluate
print("\nAccuracy:",round(accuracy_score(y_test,y_pred),4))
print("\nClassification Report:")
print(classification_report(y_test,y_pred))
