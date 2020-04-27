#import the libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

#get the dataset
dataset = pd.read_csv("Social_Network_Ads.csv")

#get the dependant and independant variables
X = dataset.iloc[: , [2,3]].values 
y = dataset.iloc[: , 4].values

#split the dataset into training and testing set
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.25 , random_state=0)

#scale the value of X into proper form
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

#create classifier object and fit the data
classifier = SVC(kernel='linear' , random_state=0)
classifier.fit(X_train , y_train)

#make the prediction
prediction = classifier.predict(X_test)

#make confusion matrix
cm = confusion_matrix(y_test, prediction)

#plot the values
#graph for the training set
X_set , y_set = X_train , y_train
X1 , X2 = np.meshgrid(np.arange(X_set[: , 0].min() - 1 , X_set[: , 0].max() + 1 , 0.01),
                      np.arange(X_set[: , 1].min() - 1 , X_set[: , 0].max() + 1 , 0.01))
plt.contourf(X1 , X2 , classifier.predict(np.array([X1.ravel() , X2.ravel()]).T).reshape(X1.shape) , alpha=0.75 , cmap = ListedColormap(("red" , "green")))
plt.xlim(X1.min() , X1.max())
plt.ylim(X2.min() , X2.max())
for i , j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] , X_set[y_set == j , 1] , c=ListedColormap(('red','green'))(i) , label=j)
plt.title("Support Vector machine (Training dataset)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()

#graph for the testing data
X_set , y_set = X_test , y_test
X1 , X2 = np.meshgrid(np.arange(X_set[: , 0].min() -1 , X_set[: , 0].max() + 1 , 0.01),
                      np.arange(X_set[: , 1].min() - 1 , X_set[: , 1].max() + 1 , 0.01))
plt.contourf(X1 , X2 , classifier.predict(np.array([X1.ravel() , X2.ravel()]).T).reshape(X1.shape) , alpha=0.75 , cmap=ListedColormap(('red' , 'green')))
plt.xlim(X1.min() , X1.max())
plt.ylim(X2.min() , X2.max())
for i , j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] , X_set[y_set == j , 1] , c = ListedColormap(('red','green'))(i) , label=j)
plt.title("Support vector machine (SVM) (Testing dataset)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()