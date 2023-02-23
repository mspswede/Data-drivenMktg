#Factor analysis

#import packages
import os
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import minimize
import copy
import matplotlib.pyplot as plt

#change directory to wherever the data file is located.
os.chdir('/Users/arun/Dropbox/Teaching/fall 2021/BUSI712/R code')
df = pd.read_excel('bank.xlsx')
print(df)
df_all = copy.deepcopy(df)
df.drop(['Id', 'Volume', 'Prin1','Prin2'],axis=1,inplace=True)

#Compute correlation matrix
corrmat = df.corr()
print(corrmat)

#eigenvalues and eigenvectors
eigpar = np.linalg.eig(corrmat)

eigvals = eigpar[0]
eigvec = -eigpar[1]
sorted_eigvals = sorted(eigvals,reverse=True)
#need to sort eigenvectors, just so happens the first two are sorted this time.

plt.scatter(range(1,len(eigvals)+1),sorted_eigvals)
plt.plot(range(1,len(eigvals)+1),sorted_eigvals)
plt.title('Scree Plot')
plt.xlabel('Factor #')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

#factor loadings (generalize to beyond 2 factors)
nFac = 2
C = eigvec[0:len(eigvals),0:nFac]
D = np.zeros((2,2))
D[0,0]=eigvals[0]
D[1,1]=eigvals[1]

#loading matrix
S_loadings = np.dot(C,scipy.linalg.sqrtm(D))

#communalities
S_h2 = np.sum(np.square(S_loadings),axis=1)

#Compute factor scores (based on pseudocode I will provide)








