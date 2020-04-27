import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataframe = pd.read_csv("Salary_Data.csv")

X = dataframe.iloc[: , 0].values
y = dataframe.iloc[: , 1].values

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=1/3 , random_state =0)

# reshape the data
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

regressor = LinearRegression()
regressor.fit(X_train , y_train)
prediction = regressor.predict(X_test)

# plot the values
plt.scatter(X_train , y_train , color="red")
plt.plot(X_train , regressor.predict(X_train) , color="green")
plt.title("Simple Regression")
plt.xlabel("Years of experiance")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test , y_test , color="red")
plt.plot(X_test , regressor.predict(X_test) , color="green")
plt.title("Simple Regression test case")
plt.xlabel("Years of Experiance")
plt.ylabel("Salary")
plt.show()
