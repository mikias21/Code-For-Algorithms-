#import libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#read the csv
dataset = pd.read_csv("Position_Salaries.csv")

#get the dependant and independant vars
X = dataset.iloc[: , 1].values
y = dataset.iloc[: , 2].values

#reshape the X and y values
X = X.reshape(-1 , 1)
y = y.reshape(-1 , 1)

#fitting linear regression model in the dataset
lin_reg = LinearRegression()
lin_reg.fit(X , y)

#fitting the polynomial regression model in the dataset
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

#again fitting the data set form x_poly into new linear regression model
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly , y)

#visualizing the linear regression model
plt.scatter(X , y , color='red')
plt.plot(X , lin_reg.predict(X) , color='green')
plt.title("Truth or Lie")
plt.xlabel("Level of experiance(Linear Regression)")
plt.ylabel("Salary")
plt.show()

#visualizing the polynomial model
# X_grid = np.arange(min(X) , max(X) , 0.1)
# X_gird = X_grid.reshape((len(X_grid) , 1))
plt.scatter(X , y , color="red")
plt.plot(X , lin_reg2.predict(poly_reg.fit_transform(X)) , color="green")
plt.title("Level of experiance(Polynomial Regression)")
plt.xlabel("Experiance")
plt.ylabel("Salary")
plt.show()

#predict using the linear Regression method
lin_pre = lin_reg.predict(np.array([6.5]).reshape(-1,1))
print("The linear regression prediction is {}".format(lin_pre))

#predict using the polynomial regression method
poly_pre = lin_reg2.predict(poly_reg.fit_transform([[6.5]]))
print("The Polynomial regression prediction is {}".format(poly_pre))
