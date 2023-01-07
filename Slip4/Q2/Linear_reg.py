
# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# %matplotlib inline
dataset=pd.read_csv('Salary_Data.csv')
print(dataset.shape)
#dataset.head(5)
#dataset.describe()in scatter plot
#data can be represented 
#dataset.plot(x='YearsExperience',y='Salary',style='*')
#plt.title('yearexp vs salary')
#plt.xlabel('Yearsofexp')
#plt.ylabel('Salary')
#Text(0,0.5,'Salary')
#dependancy linear in nature then go for Linear regression model
#convert i/p values in numpy array
x=dataset['YearsExperience'].values.reshape(-1,1)
y=dataset['Salary'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#split data into 80% training and 20% testing
#algorithm train on traning dataset using LR
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(x_test)
x_train=sc.transform(x_train)
x_test=sc.transform(x_test)
y_train=sc.transform(x_train)
y_test=sc.transform(y_test)
LR=LinearRegression()
LR.fit(x_train,y_train)
print("Intercept",LR.intercept_)#for retrive slope
print("coefficient",LR.coef_)


y_pred=LR.predict(x_test)
#scatter plot where the line indicate line of regression
plt.scatter(x_train,y_train)
plt.plot(x_test,y_pred,color='red')
plt.title("simple regression")
plt.xlabel("YerasofExp")
plt.ylabel("salary")
plt.show()
accuracy=LR.score(x_test,y_test)
print('Accurecy='+str(accuracy))
print(LR.predict([[1.2]]))
