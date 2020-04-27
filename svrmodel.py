#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR #support vector regression

#get the dataset
dataframe = pd.read_csv("Position_Salaries.csv")

#get the independant and dependant variables
X = dataframe.iloc[: , 1].values
y = dataframe.iloc[: , 2].values

#reshape the arrays
X = X.reshape(-1,1)
y = y.reshape(-1,1)

#implement feature scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#fit the data to our model
regressor = SVR(kernel='rbf') #radius basis function
regressor.fit(X , y)

#make the prediction values a numpy array and transform it into proper scale
val = np.array([6.5]).reshape(-1,1)
val = sc_X.transform(val)
prediction = regressor.predict(val)
prediction = sc_y.inverse_transform(prediction)

#plot the graph
X_grid = np.arange(min(X) , max(X) , 0.1)
X_grid = X_grid.reshape((len(X_grid) , 1))
plt.scatter(X , y , color="red")
plt.plot(X_grid , regressor.predict(X_grid) , color="green")
plt.title("truth salary (SVR model)")
plt.xlabel("level")
plt.ylabel("Salary")
plt.show()

#print out the result
print("\n\nThe prediction made is " , end="")
print(prediction)
