#import the libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

#get the dataset
dataset = pd.read_csv("Social_Network_Ads.csv")

#get depenandant and independant variables
X = dataset.iloc[: , [2,3]].values
y = dataset.iloc[: , 4].values

#split the dataset into training set and testing test
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.25 , random_state=0)

#scale the values of X_train and X_test to proper form
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

#fitting the training the data
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train , y_train)

#predict the y values
y_pred = classifier.predict(X_test)

#make confusion matrix
cm = confusion_matrix(y_test , y_pred)

#visualizing the results of the training set
X_set , y_set = X_train , y_train
#create grid for the graph
X1 , X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1 , stop = X_set[: , 0].max() + 1 , step = 0.01),
                      np.arange(start = X_set[:,1].min() -1 , stop = X_set[: , 1].max() + 1 , step = 0.01))
plt.contourf(X1 , X2 ,
            classifier.predict(np.array([X1.ravel() , X2.ravel()]).T).reshape(X1.shape) ,
            alpha = 0.75 , cmap = ListedColormap(('red' , 'green')))
#plot the X limit and y limit
plt.xlim(X1.min() , X1.max())
plt.ylim(X2.min() , X2.max())
#scatter the points
for i , j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] , X_set[y_set == j , 1] ,
                c = ListedColormap(('red','green'))(i) , label=j)
#set the title and labels
plt.title("Logistic Regression for the training data set")
plt.xlabel('Age')
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

#plot the char for the testing dataset
X_set , y_set = X_test , y_test
#create the grids for the graph
X1 , X2 = np.meshgrid(np.arange(start = X_set[:,0].min() - 1 , stop = X_set[: , 0].max() + 1 , step = 0.01),
                      np.arange(start = X_set[:,1].min() -1 , stop = X_set[: , 1].max() + 1 , step=0.01))
plt.contourf(X1 , X2 , classifier.predict(np.array([X1.ravel() , X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75 , cmap = ListedColormap(('red','green')))
#scatter the points
for i , j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] , X_set[y_set == j , 1],
                c = ListedColormap(('red','green'))(i) , label=j)
#set the title and labels
plt.title("Logistic Regression for the testing datasets")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()
