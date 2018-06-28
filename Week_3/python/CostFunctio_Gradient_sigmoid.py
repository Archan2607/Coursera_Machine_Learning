def sigmoid(z):
    return(1/(1 + np.exp(-z)))


def costFunction(theta,x,y):
    m = y.size
    h = sigmoid(x.dot(theta))
    
    J = -1*(1/m)*(np.log(h).T.dot(y)+np.log(1-h).T.dot(1-y))
               
    if np.isnan(J[0]):
        return(np.inf)
    return(J[0])


def gradient(theta, x, y):
    m = y.size
    h = sigmoid(x.dot(theta.reshape(-1,1)))
    
    grad =(1/m)*X.T.dot(h-y)

    return(grad.flatten())

i_theta = np.zeros(X.shape[1])
cost = costFunction(i_theta, X, y)
grad = gradient(i_theta, X, y)
print('Cost: \n', cost)
print('Grad: \n', grad)
