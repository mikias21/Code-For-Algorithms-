#import libs
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
#get the dataset
dataset = pd.read_csv("Mall_Customers.csv")

#get the independant variable
X = dataset.iloc[: , [3,4]].values

#plot the dandrom graph to get the correct number of clasters
dendrogram = sch.dendrogram(sch.linkage(X , method='ward'))
plt.title("Dendogram")
plt.xlabel("Customers")
plt.ylabel("Eculdian distances")
plt.show()

#fit and predict the dataset in AgglumerativeClustering
hc = AgglomerativeClustering(n_clusters= 5 , affinity='euclidean' , linkage='ward')
y_hc = hc.fit_predict(X)

#plot the graph for clustering
plt.scatter(X[y_hc == 0 , 0] , X[y_hc == 0 , 1] , c='red' , label="Careful")
plt.scatter(X[y_hc == 1 , 0] , X[y_hc == 1 , 1] , c='yellow' , label="Standard")
plt.scatter(X[y_hc == 2 , 0] , X[y_hc == 2 , 1] , c='blue' , label="target")
plt.scatter(X[y_hc == 3 , 0] , X[y_hc == 3 , 1] , c='black' , label="Careless")
plt.scatter(X[y_hc == 4 , 0] , X[y_hc == 4 , 1] , c='purple' , label='Sensible')
plt.title("Hirarchical Clustering")
plt.xlabel("Annual Income K$")
plt.ylabel("Spending Score (1 - 100)")
plt.legend()
plt.show()
