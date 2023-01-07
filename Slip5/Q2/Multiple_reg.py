
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# %matplotlib inline
df=pd.read_csv("cars.csv")
df.head(5)
x=df[['debt','income']]
y=df['sales']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
MLR=LinearRegression()
MLR.fit(x_train,y_train)
print("intercept",MLR.intercept_)
print("coefficient",MLR.coef_)
predict=MLR.predict([[418,7017]])
print(predict)
