import pandas as pd
import os
import copy
from sklearn.cluster import KMeans

os.chdir('/Users/arun/Documents/')
df = pd.read_excel('conjrel1.xlsx')

df_all = copy.deepcopy(df)
df.drop(['Customer'],axis=1,inplace=True)

#K-means clustering.
#May want to standardize variables - but factor scores already take into account.

kmeans = KMeans(init="random",n_clusters=2, n_init=100, max_iter=1000,random_state=199)

kmeans.fit(df)

print(kmeans.cluster_centers_)
print(kmeans.labels_+1)
print(kmeans.inertia_)
#Cubic clustering criterion not available I think.
