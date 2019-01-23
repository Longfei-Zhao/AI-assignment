import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from dist import dist, search
from sklearn.base import BaseEstimator, ClusterMixin, TransformerMixin
import scipy

import sample

_pathToDataset = '../data/assign_data_train/'

class KMeans(BaseEstimator, ClusterMixin, TransformerMixin):
    '''
        Custom implementation of KMeans that fits to sklearn's pipeline
    '''

    ## Don't modify this constructor
    def __init__(self, K, max_iter = 100, distance = 'cosine', tol = 1e-3):
        '''
            constructor for KMeans class

            arguments:
                - K: number of clusters
                - max_iter: max number of iterations
                - distance: distace measure to use - 'cosine' or 'euclid'
                - tol: tolerance for convergence
        '''

        assert K >= 1, ('invalid K , must be +ve')
        assert max_iter >= 1, ('invalid max_iter, must be +ve')
        assert tol > 0 and tol < 1, ('tol must be in rangd (0, 1)')

        self.K = K
        self.max_iters = max_iter
        self.dist = distance
        self.centroids = None
        self.labels = None
        self.tolerance = tol

    def init_centroids(self, X):
        '''
            this method returns the initial centroids
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - centroids: centroids matrix (k * d dims)
        '''

        n, d = X.shape
        idx = np.random.choice(n, self.K)

        return X[idx, :]

    def cost(self, X):
        '''
            this method returns the sum of distance between centroid and points for each cluster
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - dists: vector of length k where dists[i] is sum of distance
                            between centroid[i] and points that lie in cluster i
        '''
        costs = np.zeros(self.K)
        for k in range(self.K):
            ## TODO start
            ## instructions: compute the sum of the distances between documents belonging to cluster k and its centroid
            ## hint: you might want to use dist function from dist.py here

            ## TODO end
            costs[k] = dist(X[np.where(self.labels == k)[0], :], self.centroids[k], self.dist).sum()

        return costs

    def reassign(self, X):
        '''
            this method returns the new labels for each data point in X
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - labels: vector of length n where labels[i] is the
                    cluster label for ith point
        '''
        n, d = X.shape
        new_assign = np.zeros(n)
        ## TODO start
        ## instructions: compute the new assignments for each row in X
        ## hint: you might want to use dist function from dist.py here
        for i in range(n):
            new_assign[i] = np.argmin(dist(self.centroids, X[i], self.dist))
        ## TODO end
        return new_assign

    def recompute(self, X):
        '''
            this method returns new centroids
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - centroids: new centroids computed from labels
        '''
        ## TODO
        n, d = X.shape
        centroids = np.zeros((self.K, d))
        ## TODO start
        ## instructions: compute the new centroids
        for k in range(self.K):
            centroids[k] = np.average(X[np.where(self.labels == k)[0], :], 0)
        ## TODO end
        return centroids

    ## TODO: Look inside this function for instructions
    def fit(self, X, y = None):
        '''
            this method is the body of the KMeans algorithm. It regroups the data X into k clusters
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - self
        '''
        if type(X) == scipy.sparse.csr.csr_matrix:
            X = X.toarray()

        n_iter = 0
        converged = False
        ## TODO start
        ## Step 1: initialize centroids and labels
        self.centroids = self.init_centroids(X)
        self.labels = self.reassign(X)
        oldObj = self.cost(X).sum()
        ## TODO stop

        ## iterate
        while n_iter < self.max_iters and not converged:
            ## TODO start
            ## Step 2: recompute centroids, recompute new document assignation, check stopping criteria
            self.centroids = self.recompute(X)
            self.labels = self.reassign(X)
            ## TODO end
            obj = self.cost(X).sum()
            if oldObj - obj < self.tolerance:
                converged = True
            oldObj = obj
            print('iter = {}, objective = {}'.format(n_iter, obj))
            n_iter += 1

        return self

    ## TODO: Look inside this function for instructions
    def get_n_documents(self, X, n = 5):
        '''
            this method returns the index of top n documents from each cluster
            input =>
                - X input data matrix (n * d dims)
                - n: number of top documents to return
            output: =>
                - results: list of tuple (k, index) which means doc at index belongs to cluster k
        '''
        if type(X) == scipy.sparse.csr.csr_matrix:
            X = X.toarray()
        labels = self.transform(X)
        results = []
        for k in range(self.K):
            ## TODO: return either names of indexes of the top 5 documents in each cluster
            ## Hint: look inside dist.py for help on this
            idx = search(X[np.where(self.labels == k)[0], :], self.centroids[k], self.dist, n)
            for i in idx:
                results.append((k, i))
            ## TODO stop
        return results

    ## all the methods below are required for the integration with scikit-learn.
    ## DO NOT EDIT ANY METHOD BELOW HERE
    def transform(self, X, y = None):
        '''
            this method returns the labels by inferencing on fitted model
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - labels: inferred models
        '''
        if type(X) == scipy.sparse.csr.csr_matrix:
            X = X.toarray()
        return self.reassign(X)

    def fit_transform(self, X, y = None):
        '''
            this method returns the labels by fitting X to the model
            input =>
                - X : data matrix (n * d dims)
            output: =>
                - labels: inferred models
        '''
        self.fit(X)
        return self.labels

if __name__ == "__main__":

    dataset = sample.read_as_df(_pathToDataset)
    dataset['tokens'] = dataset['text'].apply(sample.preprocessor)
    print(dataset['tokens'])
