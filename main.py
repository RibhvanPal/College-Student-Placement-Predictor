import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import pickle

data=pd.read_csv("college_student_placement_dataset.csv")

data=data.drop('College_ID',axis=1)
data['Internship_Experience'] = data['Internship_Experience'].map({'No': 0, 'Yes': 1})
data['Placement'] = data['Placement'].map({'No': 0, 'Yes': 1})

X = data[['IQ', 'Prev_Sem_Result', 'CGPA', 'Academic_Performance',
          'Internship_Experience', 'Extra_Curricular_Score',
          'Communication_Skills', 'Projects_Completed']]
y = data['Placement']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
)


model = svm.SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)


