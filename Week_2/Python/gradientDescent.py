from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def gradD(X,y,theta,alpha,iterations):
    m=len(y)
    j_hist=np.zeros(iterations)
    
    for i in range(iterations):
        theta = theta - (alpha/m)*np.sum((np.dot(X,theta)-y)[:,None]*X,axis=0)
        j_hist[i] = computec(X, y, theta)
        print('Cost function: ', j_hist[i])
    
    return (theta,j_hist)
    
gradD(X,y,theta,alpha,iterations)


#plotting linear fit

plt.plot(x,y,'rx',x,np.dot(X,theta),'b-')
plt.legend(['Training Data','Linear Regression'])
plt.show()


# Predict values for population sizes of 35,000 and 70,000
predict1 = np.dot([1, 3.5],theta) # takes inner product to get y_bar
print('For population = 35,000, we predict a profit of ', predict1*10000)

predict2 = np.dot([1, 7],theta)
print('For population = 70,000, we predict a profit of ', predict2*10000)
input('Program paused. Press enter to continue.\n');
print('Visualizing J(theta_0, theta_1) ...\n')

# Grid over which we will calculate J 
theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)
J_vals = np.zeros((len(theta0_vals),len(theta1_vals)))

for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        t = np.array([theta0_vals[i],theta1_vals[j]])
        J_vals[i][j] = computec(X,y,t)

fig = plt.figure()
ax = plt.subplot(111,projection='3d')
Axes3D.plot_surface(ax,theta0_vals,theta1_vals,J_vals,cmap=cm.coolwarm)
plt.show()
fig = plt.figure()
ax = plt.subplot(111)
plt.contour(theta0_vals,theta1_vals,J_vals) 
