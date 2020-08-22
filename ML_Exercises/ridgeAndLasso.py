import numpy as np
import random as rd

def sigmoid(t):
    return 1 / (1 + np.exp(-t))
def generateData(n, m, theta):
    # Input variables
    temp_X = np.random.randn(n, m)   
    unit = np.ones([n,1], dtype = int)
    X = np.append(unit, temp_X, axis=1)
    # Parameters
    beta = np.random.randn(m+1)
    betaX = np.dot(X,beta)
    prob = sigmoid(betaX)
    
    
    # Output
    Y = np.where(prob >= theta,  1,  0)
    return X, Y, beta
def accuracy(beta, X, Y):
    betaX = np.dot(X,beta)
    prob = sigmoid(betaX)
    predictedY = np.where(prob >= 0.5,  1,  0)
    n = Y.shape[0]
    err = np.where(Y != predictedY, 0, 1)
    return np.count_nonzero(err == 1) * 100/n

def getCost(X, Y, lasso, epochs = 1000, threshold = 0.0001, learningRate = 0.01):
    prev = float('inf')
    n = X.shape[0]
    m = X.shape[1]
    beta = np.random.randn(m)
    tuningParameter = 0.01
    penalty_der = penalty = 0
    for _ in range(epochs):
        if lasso == True:
            penalty = tuningParameter*np.sum(beta[1:n] * beta[1:n])
            penalty_der = 2*tuningParameter*np.sum(beta[1:n])
        elif lasso == False:
            penalty = np.sum(abs(beta[1:n]))
            penalty_der = tuningParameter

        betaX =  np.dot(X,beta)
        predictProb = sigmoid(betaX)
        cost = -(np.sum(Y*np.log(predictProb) + (1-Y)*np.log(1-predictProb)))/n + penalty
        if abs(prev - cost) <= threshold:
            return cost, beta
        prev = cost
        der_cf = -1/n * np.dot(X.T, Y - predictProb) + penalty_der
        beta -= learningRate * der_cf
    return cost, beta
def logisticRegression(X, Y):
    return getCost(X, Y,-1)

def lassoRegression(X, Y):
    return getCost(X, Y, True)

def ridgeRegression(X, Y):
    return getCost(X, Y, False)

data = generateData(10000, 2, 0.5)
print("Original Beta", data[2])

# Getting Data size
n = data[1].shape[0]
# Defining Length of Training Data
trainLen = int(0.8*data[0].shape[0])

print("Parameters and Cost")
logisticCoeffients = logisticRegression(X = data[0][0:trainLen], Y = data[1][0:trainLen])
print("Logistic Regression", logisticCoeffients[1], logisticCoeffients[0])
lassoCoeffients = lassoRegression(X = data[0][0:trainLen], Y = data[1][0:trainLen])
print("Lasso Regression",lassoCoeffients[1], lassoCoeffients[0])
ridgeCoeffients = ridgeRegression(X =  data[0][0:trainLen], Y = data[1][0:trainLen])
print("Ridge Regression" ,ridgeCoeffients[1], ridgeCoeffients[0])

print("Accuracy")
logisticAccuracy =  accuracy(logisticCoeffients[1],data[0][trainLen:n],data[1][trainLen:n])
print("Logistic Regression", logisticAccuracy)
lassoAccuracy = accuracy(lassoCoeffients[1],data[0][trainLen:n],data[1][trainLen:n])
print("Lasso Regression", lassoAccuracy)
ridgeAccuracy = accuracy(ridgeCoeffients[1],data[0][trainLen:n],data[1][trainLen:n])
print("Ridge Regression", ridgeAccuracy )

