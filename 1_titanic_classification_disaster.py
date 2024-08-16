# -*- coding: utf-8 -*-
"""1.titanic-classification-disaster.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I2HU0VFxNT53G5f8dVHuda6RBX5qZo9x

#DEVKISHAN KHATRI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

"""###Data collection and processing"""

df= pd.read_csv("Titanic-Dataset.csv")

df.shape

df.head()

df.tail()

df.describe()

df.info()

df.isnull().sum()

"""##remove null values"""

df = df.drop(columns= 'Cabin', axis=1)

df = df.drop(columns= 'Embarked', axis=1)

df.head()

df['Age'].fillna(df['Age'].mean(), inplace = True)

df.isnull().sum()

df.head()

"""##Analysis the data"""

df.describe()



Survived = df['Survived'].value_counts().reset_index()
Survived

df['Sex'].value_counts()

male_count = (df['Sex'] == 'male').sum()
female_count = (df['Sex']== 'female').sum()
print(f'{male_count}', f'{female_count}')

male_survived = ((df['Survived'] == 1) & (df['Sex'] == 'male'))
male_survived.value_counts()

female_survived = ((df['Survived'] == 1) & (df['Sex'] == 'female'))
female_survived.value_counts()

data = {'Survived': ['Male - Yes', 'Male - No', 'Female - Yes', 'Female - No'],
        'Counts': [109, 782, 233, 658]}  # replace with actual counts
Survived = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.bar(Survived['Survived'], Survived['Counts'],color=["red","blue","green","pink"])

plt.title('Comparison of Survival')
plt.xlabel('Gender and Survival Status')
plt.ylabel('Number of People')
plt.show()

df

df.shape

"""###Encoding column"""

df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
df.head()

df.replace({'Sex':{'male': 0, 'female': 1}}, inplace=True)

inputs = df.drop('Survived',axis='columns')
target = df['Survived']

inputs

target

x_train, x_test, y_train, y_test = train_test_split(inputs , target, test_size= 0.2, random_state =2)

print(inputs.shape, x_train.shape, x_test.shape)

"""###Logistic regression and training"""

model = LogisticRegression()

model.fit(x_train, y_train)

"""###testing model"""

x_train_prediction = model.predict(x_train)

print(x_train_prediction)

train_accuracy = accuracy_score(y_train , x_train_prediction)

train_accuracy

x_test_prediction= model.predict(x_test)

test_accuracy = accuracy_score(y_test , x_test_prediction)

test_accuracy

sex=pd.get_dummies(inputs.Sex)
sex.head()

inputs=pd.concat([inputs,sex],axis="columns")
inputs.head()

inputs.drop(["Sex"],axis="columns",inplace=True)

inputs.head()

inputs.isna().sum()

inputs.Age = inputs.Age.fillna(inputs.Age.mean())
inputs.head()

inputs.info()

inputs.isna().sum()

"""Survived"""

inputs.corr()

import seaborn as sns

sns.heatmap(inputs.corr(), annot=True, cmap='coolwarm', fmt=".2f")

model=RandomForestClassifier()

model.fit(x_train,y_train)

model.score(x_test,y_test)

pre=model.predict(x_test)

matrices=r2_score(pre,y_test)
matrices

"""#Thank you

"""