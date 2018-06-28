from scipy.optimize import minimize

#Minimization of scalar function of one or more variables.

res = minimize(costFunction, i_theta, args=(X,y), method=None, jac=gradient, options={'maxiter':400})
res

#scipy.optimize.minimize(fun, x0:- Initial guess, args=(): - Extra arguments passed to the objective function and its derivatives (Jacobian, Hessian)., method=None, jac: - Jacobian (gradient) of objective function, hess=None, hessp=None, bounds=None, constraints=(), tol=None, callback=None, options=None)[source]


def predict(theta, X, threshold=0.5):
    p = sigmoid(X.dot(theta.T)) >= threshold
    return(p.astype('int'))

# Student with Exam 1 score 45 and Exam 2 score 85
# Predict using the optimized Theta values from above (res.x)
sigmoid(np.array([1, 45, 85]).dot(res.x.T))


p = predict(res.x, X) 
print('Train accuracy {}%'.format(100*sum(p == y.ravel())/p.size))

plt.scatter(45, 85, s=60, c='r', marker='v', label='(45, 85)')
plotData(data, 'Exam 1 score', 'Exam 2 score', 'Admitted', 'Not admitted')
x1_min, x1_max = X[:,1].min(), X[:,1].max(),
x2_min, x2_max = X[:,2].min(), X[:,2].max(),
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
h = sigmoid(np.c_[np.ones((xx1.ravel().shape[0],1)), xx1.ravel(), xx2.ravel()].dot(res.x))
h = h.reshape(xx1.shape)
plt.contour(xx1, xx2, h, [0.5], linewidths=1, colors='b');
