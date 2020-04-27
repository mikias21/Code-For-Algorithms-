#import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

#read the data
dataframe = pd.read_csv("Position_Salaries.csv")

#get the dependant and independant
X = dataframe.iloc[: , 1].values
y = dataframe.iloc[: , 2].values

#reshape the data
X = X.reshape(-1,1)
y = X.reshape(-1,1)

#train and fit the data
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X , y)

#plot the graph
#make the graph more prefect
X_grid = np.arange(min(X) , max(X) , 0.01)
X_grid = X_grid.reshape((len(X_grid) , 1))
plt.scatter(X , y , color="red")
plt.plot(X_grid , regressor.predict(X_grid) , color="green")
plt.title("Prediction using Regression Tree")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

sal_pred = regressor.predict(np.array([6.5]).reshape(-1,1))
print(sal_pred)
