import numpy as np 
import random as rd

def generateData(std, n, m):
    temp_X = np.random.rand(n, m)       # m Independent Variables 
    unit = np.ones([n,1], dtype = int)
    X = np.append(unit, temp_X, axis=1) # adding column with value
    beta = np.random.rand(m+1)
    e = rd.gauss(0, std)                # unexplained varience
    Y = np.matmul(X,beta)  + e
    print("Original Beta",beta)
    return X, Y, beta

def linearRegression(X,Y,step_size, threshold,k):
    m = X.shape[1]
    beta = np.random.rand(m)
    prev = float('inf')
    for _ in range(k):
        Yi = np.matmul(X,beta)
        E = Y - Yi
        cf = np.dot(E, E)
        if abs(prev - cf) <= threshold:
            return cf, beta
        prev = cf
        der_cf = -(2 *  np.matmul(E,X))
        beta -= step_size * der_cf
      
    print("Run Completly") 
    return cf, beta

data = generateData(0.56,4800, 4)
predictions = linearRegression(data[0], data[1], 0.0001 , 0.01,500)

print("Predicted Beta",predictions[1])
print("Cost Function",predictions[0])

dot_beta = np.dot(data[2], predictions[1])
given_norm = np.linalg.norm(data[2])
predicted_norm = np.linalg.norm(predictions[1])
cos_sim = dot_beta / (given_norm * predicted_norm) 
print(cos_sim)