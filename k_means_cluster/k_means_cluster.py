import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale
from sklearn import metrics


def bench_k_means(estimator, name, data, y):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y, estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_, metric='euclidean')))

# # implement a simple key means cluster algorithm
# def k_means_cluster(data, k):
#     # create a k-means model
#     model = KMeans(n_clusters=k, random_state=1, n_init=10
#     # fit the model to the data
#     model.fit(data)
#     # return the cluster assignments
#
#     return model.labels_

def main():
    # read in the data
    digits = load_digits()
    data = scale(digits.data)
    y = digits.target

    k = len(np.unique(y))

    samples, features = data.shape

    model = KMeans(n_clusters=k, random_state=1, n_init=10)

    bench_k_means(model, "1", data, y)



    #
    # # create a list of the labels
    # labels = ['label']
    # # fit the model
    # cluster_assignments = k_means_cluster(data[features], 2)
    # # create a scatter plot for the data
    # plt.scatter(data['x'], data['y'], c=cluster_assignments)
    # # show the plot
    # plt.show()
    # # calculate the silhouette score
    # score = silhouette_score(data[features], cluster_assignments)
    # # print the score
    # print(score)

main()