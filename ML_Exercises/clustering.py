from sklearn.datasets import make_blobs, make_moons, make_circles
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np

def generateData(samples, features, clusters):
    # Generate blobs
    xVector, labels = make_blobs(n_samples = samples, n_features = features, centers = clusters)
    return xVector, labels
    """
    # Generate circles
    xVector, labels = make_circles(n_samples=samples, noise=0.05)
    # Generate moons
    xVector, labels = make_moons(n_samples=samples, noise=0.1)
    """
# Scale dimensions between 0 and 1 
def scale(xVector):
    xMin = np.amin(xVector, axis=0)
    xMax = np.amax(xVector, axis=0)
    return (xVector - xMin)/(xMax - xMin)

def plotClusters(xVectorScaled,centroids):
    # Plotting clusters with different colors
    df = DataFrame(dict(x=xVectorScaled.T[0], y=xVectorScaled.T[1], label=labels))
    colors = {0:'red', 1:'cyan', 2:'green', 3:'yellow', 4:'pink',5:'cyan'}
    fig, ax = plt.subplots()
    grouped = df.groupby('label')
    for key, group in grouped:
        group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
    plt.scatter(*centroids.T)
    plt.show()

    """
    # Plotting Clusters with same colors
    plt.scatter(*xVectorScaled.T)
    plt.scatter(*centroids.T)
    plt.show()
    """

def kMeans(xVector, k, epochs, threshold):
    xVectorScaled = scale(xVector)
    features = xVectorScaled.shape[1]
    rowCount = xVectorScaled.shape[0]

    # Initializing Centroids 
    # Random Selection of Centroids from the Data
    randomIdx = np.random.choice(rowCount, size = k, replace = False)
    centroids = xVectorScaled[randomIdx, :]
    print("Initial Centroids")
    print(centroids)

    # Plotting Clusters and Initial Centroids
    plotClusters(xVectorScaled, centroids)

    # Running k-means for given iterations
    for _ in range(epochs):
        # Dictionary to store data points associated with the particular centroids
        labeledData = {}
        for label in range(k):
            labeledData[label] = []      # labeledData[i] = [np.array([0,0])] --> Required when randomnly chosen Centroids are not from the Data
        
        # Compute Distance of each point in Data from the defined Centroids
        for value in xVectorScaled:
            distance = [np.linalg.norm(value - centroids[i]) for i in range(k)]
            label = distance.index(min(distance))
            labeledData[label].append(value)

        # Updating Centroids
        updatedCentroids = np.empty(shape=(k, features))
        for label in range(k):
            updatedCentroids[label] = np.average(labeledData[label], axis = 0)
        
        # Exiting Loop/method if Centroids do not change much
        if (abs(centroids - updatedCentroids)).all() <= threshold:
            # Plotting Clusters and Final Centroids
            plotClusters(xVectorScaled,updatedCentroids)
            return updatedCentroids

        centroids = updatedCentroids
    # Plotting Clusters and Final Centroids
    plotClusters(xVectorScaled,centroids)
    return centroids

if __name__ == '__main__':
    xVector, labels = generateData(samples = 10000, features = 2, clusters = 3)
    centroids = kMeans(xVector, k = 3, threshold = 0.0001, epochs = 50)
    print("Final Centroids \n", centroids)