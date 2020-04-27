#import libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

#get the dataset
dataset = pd.read_csv("Social_Network_Ads.csv")

#get the dependant and independant vars
X = dataset.iloc[: , [2,3]].values
y = dataset.iloc[: , 4].values

#split the dataset into train and test
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.25 , random_state=0)

#scale the X values so that the graph will be plotted in high resolution
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

#fit the data into the classifier object
classifier = DecisionTreeClassifier(criterion='entropy' , random_state=0)
classifier.fit(X_train , y_train)
#make prediction
y_pred = classifier.predict(X_test)

#make confusion metrix
cm = confusion_matrix(y_test , y_pred)

#draw the graph

#training dataset
X_set , y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(X_set[: , 0].min() - 1 , X_set[: , 0].max() + 1 , 0.01),
                     np.arange(X_set[: , 1].min() - 1 , X_set[: , 1].max() + 1 , 0.01))
plt.contourf(X1 , X2 , classifier.predict(np.array([X1.ravel() , X2.ravel()]).T).reshape(X1.shape) , alpha=0.75 , cmpa = ListedColormap(('red','green')))
plt.xlim(X1.min() , X1.max())
plt.ylim(X2.min() , X2.max())
for i , j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] , X_set[y_set == j , 1] , c = ListedColormap(('red','green'))(i) , label=j)
plt.title("Decision Tree Classifier (Training Data set)")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()

#testing dataset
X_set , y_set = X_test , y_test
X1 , X2 = np.meshgrid(np.arange(X_set[: , 0].min() - 1 , X_set[: , 1].max() + 1 , 0.01) ,
                      np.arange(X_set[: , 0].min() - 1 , X_set[: , 1].max() + 1 , 0.01))
plt.contourf(X1 , X2 , classifier.predict(np.array([X1.ravel() , X2.ravel()]).T).reshape(X1.shape) , alpha=0.75 , cmap = ListedColormap(('red','green')))
plt.xlim(X1.min() , X1.max())
plt.ylim(X2.min() , X2.max())
for i , j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j , 0] , X_set[y_set == j , 1] , c = ListedColormap(('red','green'))(i) , label=j)
plt.title("Decision Tree Classifier (Testing Date set)")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()
plt.show()