import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

#Load and prepare data
df=pd.read_csv("cleaned_loan_data.csv")

#Encode text columns
le=LabelEncoder()
text_columns=["person_home_ownership","loan_intent","loan_grade","cb_person_default_on_file",]

for column in text_columns:
    df[column]=le.fit_transform(df[column])

#Split features and target
X=df.drop("loan_status",axis=1)
y=df["loan_status"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print("Data ready for training")
print("Training set:",X_train.shape)
print("Testing set:",X_test.shape)

# Train Random Forest model
rf_model=RandomForestClassifier(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)
print("Random Forest trained successfully")

#Make predictions
y_pred=rf_model.predict(X_test)

#Evaluate
print("\nAccuracy:", round(accuracy_score(y_test,y_pred),4))
print("\nClassififcation Report:")
print(classification_report(y_test,y_pred))

#Train with class weighting to improve recall
rf_balanced=RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)
rf_balanced.fit(X_train,y_train)
print("\nBalanced Random Forest trained")

y_pred_balanced=rf_balanced.predict(X_test)

print("Accuracy:",round(accuracy_score(y_test,y_pred_balanced),4))
print("\nClassification Report:")
print(classification_report(y_test,y_pred_balanced))


#Feature importance
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

feature_names=X.columns
importances=rf_model.feature_importances_

#Sort by importance
feature_df=pd.DataFrame({
    "feature":feature_names,
    "importance":importances
}).sort_values("importance",ascending=False)

print("\nFeature Importance:")
print(feature_df)

#plot
plt.figure(figsize=(10,6))
plt.barh(feature_df["feature"],feature_df["importance"])
plt.title("Feature Importance - Random Forest")
plt.xlabel("Importance Score ")
plt.gca().invert_yaxis()
plt.savefig("feature_importance.png")
print("\nFeature importance chart saved")