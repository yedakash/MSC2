#polynomial regression
import numpy as np 
import matplotlib.pyplot as mtp
import pandas as pd
dataset=pd.read_csv('Position_Salaries.csv')
print(dataset)
x=dataset.iloc[:,1:2].values
#print(x)
y=dataset.iloc[:,2].values
print(y)
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
lin=LinearRegression()
lin.fit(x,y)
mtp.scatter(x,y,color='blue')
mtp.plot(x,lin.predict(x),color="red")
mtp.title("salary estimate")
mtp.xlabel("Position Levels")
mtp.ylabel("salary")
mtp.show()
from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)
lin_reg=LinearRegression()
lin_reg.fit(x_poly,y)
mtp.scatter(x,y,color='blue')
mtp.plot(x,linreg.predict(x_poly),color="red")
mtp.title("salary estimate")
mtp.xlabel("Position Levels")
mtp.ylabel("salary")
mtp.show()
