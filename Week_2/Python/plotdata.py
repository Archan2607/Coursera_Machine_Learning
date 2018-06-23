import pandas as pd
import matplotlib.pyplot as plt

def plotd(x,y):
    plt.plot(x,y,'rx')


f=pd.read_csv("..\data.txt")
a=f.iloc[:,0]
b=f.iloc[:,1]
m=len(b)

plotd(a,b)
