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
    # Calculating Probability
    prob = sigmoid(betaX)
    # Generating Labels
    Y = np.where(prob >= 0.5,  1,  0)
    for idx in range(int(n*theta)):         # Flipping Labels
        Y[idx] = 1 - Y[idx]
    return X, Y, beta

def logisticRegression(X, Y, epochs, threshold, learningRate):
    m = X.shape[1]
    n = X.shape[0]
    beta = np.random.randn(m)
    prev = float('inf')                
    # Gradient Descent
    for _ in range(epochs):
        betaX =  np.dot(X,beta)
        predictProb = sigmoid(betaX)
        cost = -(np.sum(Y*np.log(predictProb) + (1-Y)*np.log(1-predictProb)))/n
        if abs(prev - cost) <= threshold:
            return cost, beta
        prev = cost
        der_cf = -1/n * np.dot(X.T, Y - predictProb)
        beta -= learningRate * der_cf
    print("Run Completely") 
    return cost, beta

# Genarating Data
data = generateData(10000, 3, 0.1)
print("Original Beta", data[2])

# Predicting Beta and Computing Cost
predictions = logisticRegression(X = data[0], Y = data[1], epochs = 1000, threshold = 0.0001, learningRate = 0.01 )
print("Predicted Beta",predictions[1])
print("Cost",predictions[0])

# Calculating Cosine Similarity
dot_beta = np.dot(data[2], predictions[1])
given_norm = np.linalg.norm(data[2])
predicted_norm = np.linalg.norm(predictions[1])
cos_sim = dot_beta / (given_norm * predicted_norm) 
print("Cosine Similarity", cos_sim)

