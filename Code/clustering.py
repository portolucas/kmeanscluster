import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import metrics
import matplotlib.pyplot as plt


#Reader
data = pd.read_csv('monthour.csv', sep = ';', error_bad_lines=False)
x = data.iloc[:, 0:2].values

#Preprocessing
scaler = preprocessing.StandardScaler().fit(data[['HOUR']])
data['HOUR'] = scaler.transform(data[['HOUR']])

scaler = preprocessing.StandardScaler().fit(data[['MONTH']])
data['MONTH'] = scaler.transform((data[['MONTH']]))

#K-Means Cluster
kmeans = KMeans(n_clusters=3, init='random')
kmeans.fit(x)
kmeans.cluster_centers_

distance = kmeans.fit_transform(x)
labels = kmeans.labels_
print(labels)

#Elbow for perfect K

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters= i, init='random')
    kmeans.fit(x)
    print(i, kmeans.inertia_)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('O Método Elbow')
plt.xlabel('O número de clusters')
plt.ylabel('WSS') #within cluster sum of squares
print(plt.show())

# Graph with centroids and clusters
plt.scatter(x[:, 0], x[:, 1], s = 3, c = kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='red', label='Centroids')
plt.title('Month and hour of Boston Crimes in 2018 and Centroids')
plt.xlabel('MONTH')
plt.ylabel('HOUR')
plt.legend()
plt.show()

# Metric of K with Calinski and Harabaz Score
distortions = []

K = range(2,5)

for k in K:
    print(k)
    kModel = KMeans(n_clusters=k).fit(data)
    kModel.fit(data)
    distortions.append(metrics.calinski_harabaz_score(data, kModel.labels_))

plt.plot(K, distortions, 'bx-')
plt.title('Metric of K with Calinski and Harabaz Score')
plt.xlabel('k')
plt.ylabel('CH')
plt.show()








