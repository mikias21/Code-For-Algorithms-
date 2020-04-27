#import the libs
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#get the dataset
dataset = pd.read_csv("Mall_Customers.csv")

#get the independant variable
X = dataset.iloc[: , [3,4]].values

#calculate the WCSS and plot a graph to get the right number of clusters (The elbow method)
wcss = []
for i in range(1 , 11):
    kmeans = KMeans(n_clusters=i , init='k-means++' , max_iter=300 , n_init=10 , random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
#plot the graph to find the elbow
plt.plot(range(1,11) , wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()

#now fit and make prediction with the right number of clusters
kmeans = KMeans(n_clusters=5 , init='k-means++' , max_iter=300 , n_init=10 , random_state=0)
y_kmeans = kmeans.fit_predict(X)

#plot the real graph
plt.scatter(X[y_kmeans == 0 , 0] , X[y_kmeans == 0 , 1] , s = 100 , c="red" , label="Careful")
plt.scatter(X[y_kmeans == 1 , 0] , X[y_kmeans == 1 , 1] , s = 100 , c="green" , label="Standard")
plt.scatter(X[y_kmeans == 2 , 0] , X[y_kmeans == 2 , 1] , s=100 , c="purple" , label="target")
plt.scatter(X[y_kmeans == 3, 0] ,  X[y_kmeans == 3 , 1 ] , s = 100 , c="blue" , label="careless")
plt.scatter(X[y_kmeans == 4 , 0] , X[y_kmeans == 4 , 1] , s = 100 , c="magenta" , label="sensable")
plt.scatter(kmeans.cluster_centers_[: , 0] , kmeans.cluster_centers_[: , 1] , s = 300 , c = "yellow" , label="Centroids")
plt.title("Cluster of clients")
plt.xlabel("Annual Income (K$)")
plt.ylabel("Spending score(1 - 100)")
plt.legend()
plt.show()