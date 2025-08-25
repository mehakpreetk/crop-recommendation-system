import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

df=pd.read_csv("data/Crop_recommendation.csv")

le=LabelEncoder()
df['label']=le.fit_transform(df['label'])

x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=LogisticRegression()
model.fit(x_train,y_train)

joblib.dump(model,"model.pkl")
joblib.dump(scaler,"scaler.pkl")
joblib.dump(le,"encodings.pkl")
