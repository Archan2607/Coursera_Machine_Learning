import numpy as np

def computec(j,l,theta):
    m=len(l)
    
    c = (np.sum((np.dot(j,theta) - l)**2))/(2*m)
    return c
    
data = pd.read_csv("..\data.txt",names=["X","y"])
x = np.array(data.X)[:,None]
y = np.array(data.y) 
m = len(y) 

ones = np.ones_like(x) 
X = np.hstack((ones,x)) # Add a column of ones to x. hstack means stacking horizontally i.e. columnwise
theta = np.zeros(2) 
iterations = 1500
alpha = 0.01
computec(X, y, theta)


