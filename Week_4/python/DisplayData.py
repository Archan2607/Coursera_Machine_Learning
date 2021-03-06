# %load ../../../standard_import.txt
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# load MATLAB files
from scipy.io import loadmat

data = loadmat('E:\Archan\Study\Mtech\ML_Tuts\Coursera_ML\python\ex3\ex3data1.mat')
data.keys()

weights = loadmat('E:\Archan\Study\Mtech\ML_Tuts\Coursera_ML\python\ex3\ex3weights.mat')
weights.keys()

y = data['y']
# Add constant for intercept
X = np.c_[np.ones((data['X'].shape[0],1)), data['X']]

print('X: {} (with intercept)'.format(X.shape))
print('y: {}'.format(y.shape))

theta1, theta2 = weights['Theta1'], weights['Theta2']

print('theta1: {}'.format(theta1.shape))
print('theta2: {}'.format(theta2.shape))

sample = np.random.choice(X.shape[0], 20)
plt.imshow(X[sample,1:].reshape(-1,20).T)
plt.axis('off');
