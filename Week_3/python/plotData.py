import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt




#data = pd.read_csv('E:\Archan\Study\Mtech\ML_Tuts\Coursera_ML\python\ex2\ex2data2.txt',names=["x","y","z"])

def loaddata(file, delimeter):
    data = np.loadtxt(file, delimiter=delimeter)
    print('Dimensions: ',data.shape)
    print(data)
    return(data)

data = loaddata('E:\Archan\Study\Mtech\ML_Tuts\Coursera_ML\python\ex2\ex2data1.txt', ',')

X = np.c_[np.ones((data.shape[0],1)), data[:,0:2]]
y = np.c_[data[:,2]]

#np.c_: -Translates slice objects to concatenation along the second axis.

print(x,y)

import matplotlib as mpl
import matplotlib.pyplot as plt


def plotData(data, label_x, label_y, label_pos, label_neg, axes=None):
    # Get indexes for class 0 and class 1
    neg = data[:,2] == 0
    pos = data[:,2] == 1
    
    
    # If no specific axes object has been passed, get the current axes.
    if axes == None:
        axes = plt.gca()
    axes.scatter(data[pos][:,0], data[pos][:,1], marker='+', c='k', s=60, linewidth=2, label=label_pos)
    
    #axes.scatter(x,y,marker:-The marker style. marker can be either an instance of the class or the text shorthand for a particular marker. See markers for more information marker styles.,c:-color, sequence, or sequence of color, optional, default: ‘b’)
    axes.scatter(data[neg][:,0], data[neg][:,1], c='y', s=60, label=label_neg)
    axes.set_xlabel(label_x)
    axes.set_ylabel(label_y)
    axes.legend(frameon= True, fancybox = True)
    
    #frameon:- Control whether round edges should be enabled around the FancyBboxPatch which makes up the legend’s background. Default is None, which will take the value from rcParams["legend.fancybox"].
    #fancybox: - Control whether round edges should be enabled around the FancyBboxPatch which makes up the legend’s background. Default is None, which will take the value from rcParams["legend.fancybox"].
plotData(data, 'Exam 1 score', 'Exam 2 score', 'Admitted', 'Not admitted')
