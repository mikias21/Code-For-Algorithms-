#import the libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

#get the dataframe
dataframe = pd.read_csv("Position_Salaries.csv")

#get dependant and independant values
X = dataframe.iloc[:,1].values.reshape(-1,1)
y = dataframe.iloc[:,2].values.reshape(-1,1)

#create regressor object
regressor = RandomForestRegressor(n_estimators=10 , random_state=0)
regressor.fit(X , y)

#plot the dataset and the prediction
X_grid = np.arange(min(X) , max(X) , 0.01)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X , y , color="red")
plt.plot(X_grid , regressor.predict(X_grid) , color="green")
plt.title("Level Vs Salary (Random Forest Regression)")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

val = np.array([6.5]).reshape(-1,1)
prediction = regressor.predict(val)
print("\n\n the prediction is ")
print(prediction)
