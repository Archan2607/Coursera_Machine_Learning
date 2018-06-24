def gradD(X,y,theta,alpha,iterations):
    m=len(y)
    j_hist=np.zeros(iterations)
    
    for i in range(iterations):
        theta = theta - (alpha/m)*np.sum((np.dot(X,theta)-y)[:,None]*X,axis=0)
        j_hist[i] = computec(X, y, theta)
        print('Cost function: ', j_hist[i])
    
    return (theta,j_hist)
    
gradD(X,y,theta,alpha,iterations)
