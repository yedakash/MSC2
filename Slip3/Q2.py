#Categeriacl values:

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
iris = pd.read_csv("iris.csv")
iris = iris.drop('Id',axis=1)

le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
iris.Species = le.fit_transform(iris.Species)
x = iris.iloc[:, :-1].values
y = iris.iloc[:, 4].values

plt.scatter(x[:,0], x[:, 3], c=y, cmap ='flag')
plt.xlabel('Sepal Length cm')
plt.ylabel('Petal Width cm')
plt.show()

