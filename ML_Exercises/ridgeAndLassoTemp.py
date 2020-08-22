import numpy as np
import random as rd

def sigmoid(t):
    return 1 / (1 + np.exp(-t))
def generateData(n, m, theta):
    # Input variables
    temp_X = np.random.randn(n, m)   
    unit = np.ones([n,1], dtype = int)
    X = np.append(unit, temp_X, axis=1)

    # Bias
    beta = np.random.randn(m+1)
    betaX = np.dot(X,beta)
    prob = sigmoid(betaX)
    print("Original Beta", beta)
    # Output
    Y = np.where(prob >= theta,  1,  0)
    
    return X, Y, beta

def logisticRegression(X, Y,beta, epochs = 1000, threshold = 0.0001, learningRate = 0.01):
    prev = float('inf')
    n = X.shape[0]
    for _ in range(epochs):
        betaX =  np.dot(X,beta)
        predictProb = sigmoid(betaX)
        cost = -(np.sum(Y*np.log(predictProb) + (1-Y)*np.log(1-predictProb)))/n 
        if abs(prev - cost) <= threshold:
            return cost, beta
        prev = cost
        der_cf = -1/n * np.dot(X.T, Y - predictProb)
        beta -= learningRate * der_cf
    print("Run Completly") 
    return cost, beta

def lassoRegression(X, Y,beta, epochs = 1000, threshold = 0.0001, learningRate = 0.01, tunningParameter = 0.01):
    n = X.shape[0]
    prev = float('inf')
    for _ in range(epochs):
        betaX =  np.dot(X,beta)
        predictProb = sigmoid(betaX)
        cost = -(np.sum(Y*np.log(predictProb) + (1-Y)*np.log(1-predictProb)))/n + tunningParameter*np.sum(beta[1:n] * beta[1:n])
        if abs(prev - cost) <= threshold:
            return cost, beta
        prev = cost
        der_cf = -1/n * np.dot(X.T, Y - predictProb) + 2*tunningParameter*np.sum(beta[1:n])
        beta -= learningRate * der_cf
    print("Run Completly") 
    return cost, beta
def ridgeRegression(X, Y,beta, epochs = 1000, threshold = 0.0001, learningRate = 0.01, tunningParameter = 0.01):
    prev = float('inf')
    n = X.shape[0]
    print(beta[1:n] * beta[1:n])
    for _ in range(epochs):
        betaX =  np.dot(X,beta)
        predictProb = sigmoid(betaX)
        cost = -(np.sum(Y*np.log(predictProb) + (1-Y)*np.log(1-predictProb)))/n + np.sum(abs(beta[1:n]))
        if abs(prev - cost) <= threshold:
            return cost, beta
        prev = cost
        der_cf = -1/n * np.dot(X.T, Y - predictProb) + tunningParameter
        beta -= learningRate * der_cf
    print("Run Completly") 

    return cost, beta

data = generateData(10, 2, 0.5)
m = data[0].shape[1]
beta = np.random.randn(m)

logisticPredictions = logisticRegression(X = data[0], Y = data[1], beta = beta)
print(logisticPredictions)
lassoPredictions = lassoRegression(X = data[0], Y = data[1], beta = beta)
print(lassoPredictions)
ridgePredictions = ridgeRegression(X = data[0], Y = data[1], beta = beta)
print(ridgePredictions)
