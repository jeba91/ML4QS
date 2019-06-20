##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 5                                               #
#                                                            #
##############################################################

from util.VisualizeDataset import VisualizeDataset
from Chapter5.DistanceMetrics import InstanceDistanceMetrics
from Chapter5.DistanceMetrics import PersonDistanceMetricsNoOrdering
from Chapter5.DistanceMetrics import PersonDistanceMetricsOrdering
from Chapter5.Clustering import NonHierarchicalClustering
from Chapter5.Clustering import HierarchicalClustering
import copy
import pandas as pd
import matplotlib.pyplot as plot
import util.util as util


# Of course we repeat some stuff from Chapter 3, namely to load the dataset

DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sure the index is of the type datetime.
dataset_path = './intermediate_datafiles/'

try:
    dataset = pd.read_csv(dataset_path + 'chapter4_result.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e
dataset.index = dataset.index.to_datetime()

# printing = ['acc_Acceleration x (m/s^2)', 'acc_Acceleration y (m/s^2)', 'acc_Acceleration z (m/s^2)']
# printing = ['gyr_Gyroscope x (rad/s)', 'gyr_Gyroscope y (rad/s)', 'gyr_Gyroscope z (rad/s)']
# printing = ['linacc_Linear Acceleration x (m/s^2)', 'linacc_Linear Acceleration y (m/s^2)', 'linacc_Linear Acceleration z (m/s^2)']
# printing = ['mag_Magnetic field x (muT)', 'mag_Magnetic field y (muT)', 'mag_Magnetic field z (muT)']

params = [['acc_Acceleration x (m/s^2)', 'acc_Acceleration y (m/s^2)', 'acc_Acceleration z (m/s^2)', 'acc_Acceleration'],
        ['gyr_Gyroscope x (rad/s)', 'gyr_Gyroscope y (rad/s)', 'gyr_Gyroscope z (rad/s)', 'gyr_Gyroscope'],
        ['linacc_Linear Acceleration x (m/s^2)', 'linacc_Linear Acceleration y (m/s^2)', 'linacc_Linear Acceleration z (m/s^2)', 'linacc_Linear Acceleration'],
        ['mag_Magnetic field x (muT)', 'mag_Magnetic field y (muT)', 'mag_Magnetic field z (muT)', 'mag_Magnetic field']]

# First let us use non hierarchical clustering.

clusteringNH = NonHierarchicalClustering()

# Let us look at k-means first.


#
## Do some initial runs to determine the right number for k
#

for printing in params:
    # print '===== kmeans clustering ====='
    k_values = range(2, 10)
    silhouette_values = []
    for k in k_values:
        # print 'k = ', k
        dataset_cluster = clusteringNH.k_means_over_instances(copy.deepcopy(dataset), [printing[0], printing[1], printing[2]], k, 'default', 20, 10)
        silhouette_score = dataset_cluster['silhouette'].mean()
        # print 'silhouette = ', silhouette_score
        silhouette_values.append(silhouette_score)

    # plot.plot(k_values, silhouette_values, 'b-')
    # plot.xlabel('k')
    # plot.ylabel('silhouette score')
    # plot.ylim([0,1])
    # plot.show()

    # print(silhouette_values)
    # And run the knn with the highest silhouette score
    k = k_values[silhouette_values.index(max(silhouette_values))]
    print(printing[3], k, max(silhouette_values))

    dataset = clusteringNH.k_means_over_instances(copy.deepcopy(dataset), [printing[0], printing[1], printing[2]], k, 'default', 50, 50)
    # DataViz.plot_clusters_3d(dataset_knn, [printing[0], printing[1], printing[2]], 'cluster', ['label'])
    # DataViz.plot_silhouette(dataset_knn, 'cluster', 'silhouette')
    # util.print_latex_statistics_clusters(dataset_knn, 'cluster', [printing[0], printing[1], printing[2]], 'label')
    dataset = dataset.rename(index=str, columns={"cluster": "cluster_" + printing[3]})
    del dataset['silhouette']

for col in dataset.columns:
    print(col)

# k_values = range(2, 10)
# silhouette_values = []
#
# # Do some initial runs to determine the right number for k
#
# print '===== k medoids clustering ====='
# for k in k_values:
#     print 'k = ', k
#     dataset_cluster = clusteringNH.k_medoids_over_instances(copy.deepcopy(dataset), [printing[0], printing[1], printing[2]], k, 'default', 20, n_inits=10)
#     silhouette_score = dataset_cluster['silhouette'].mean()
#     print 'silhouette = ', silhouette_score
#     silhouette_values.append(silhouette_score)
#
# plot.plot(k_values, silhouette_values, 'b-')
# plot.ylim([0,1])
# plot.xlabel('k')
# plot.ylabel('silhouette score')
# plot.show()
#
# # And run k medoids with the highest silhouette score
#
# k = k_values[silhouette_values.index(max(silhouette_values))]
# # k = 5
#
# dataset_kmed = clusteringNH.k_medoids_over_instances(copy.deepcopy(dataset), [printing[0], printing[1], printing[2]], k, 'default', 20, n_inits=50)
# DataViz.plot_clusters_3d(dataset_kmed, [printing[0], printing[1], printing[2]], 'cluster', ['label'])
# DataViz.plot_silhouette(dataset_kmed, 'cluster', 'silhouette')
# util.print_latex_statistics_clusters(dataset_kmed, 'cluster', [printing[0], printing[1], printing[2]], 'label')
#
# # And the hierarchical clustering is the last one we try
#
# clusteringH = HierarchicalClustering()
#
# k_values = range(2, 10)
# silhouette_values = []
#
# # Do some initial runs to determine the right number for the maximum number of clusters.
#
# print '===== agglomaritive clustering ====='
# for k in k_values:
#     print 'k = ', k
#     dataset_cluster, l = clusteringH.agglomerative_over_instances(copy.deepcopy(dataset), [printing[0], printing[1], printing[2]], k, 'euclidean', use_prev_linkage=True, link_function='ward')
#     silhouette_score = dataset_cluster['silhouette'].mean()
#     print 'silhouette = ', silhouette_score
#     silhouette_values.append(silhouette_score)
#     if k == k_values[0]:
#         DataViz.plot_dendrogram(dataset_cluster, l)
#
# plot.plot(k_values, silhouette_values, 'b-')
# plot.ylim([0,1])
# plot.xlabel('max number of clusters')
# plot.ylabel('silhouette score')
# plot.show()

# And we select the outcome dataset of the knn clustering....

dataset.to_csv(dataset_path + 'chapter5_final.csv')
