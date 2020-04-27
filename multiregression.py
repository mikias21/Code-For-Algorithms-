# import the libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.regression.linear_model as smm

# read the data
dataset = pd.read_csv("50_Startups.csv")

# get the dependant and independant vars
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# encode the independant data
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# avoiding the dummy variable trap
X = X[:, 1:]

# split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# fit the the training data into the linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# make prediction
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination ion model
# create one more column with values of 1
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)

# starting backward elimination
# getting all the independant variables
X_opt = X[:, [0, 1, 2, 3, 4, 5]]

# creating regressor and fitting the data for the OLS method
regressor_OLS = smm.OLS(endog=y, exog=X_opt).fit()

# to get the whole summary of the model
# print(regressor_OLS.summary())

# the steps below are being done again as backward elimination method
X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = smm.OLS(endog=y, exog=X_opt).fit()
# print(regressor_OLS.summary())

# do again the backward elimination
X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = smm.OLS(endog=y, exog=X_opt).fit()
# print(regressor_OLS.summary())

# do again the backward elimination
X_opt = X[:, [0, 3, 5]]
regressor_OLS = smm.OLS(endog=y, exog=X_opt).fit()
# print(regressor_OLS.summary())

# do again the backward elimination
X_opt = X[:, [0, 3]]
regressor_OLS = smm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())
# print(X)
