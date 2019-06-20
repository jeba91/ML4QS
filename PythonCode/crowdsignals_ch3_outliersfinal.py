##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 3                                               #
#                                                            #
##############################################################

from util.VisualizeDataset import VisualizeDataset
from Chapter3.OutlierDetection import DistributionBasedOutlierDetection
from Chapter3.OutlierDetection import DistanceBasedOutlierDetection
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pylab

# Let is create our visualization class again.
DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sture the index is of the type datetime.
dataset_path = './intermediate_datafiles/'
try:
    dataset = pd.read_csv(dataset_path + 'chapter2_final2hz.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e

dataset.index = dataset.index.to_datetime()

# fig, ax = plt.subplots(5, 3)
# i = 0
# j = 0
#
# for col in [c for c in dataset.columns if not 'label' in c]:
#     sm.qqplot(dataset[col].values, line='s', ax = ax[i,j])
#     ax[i,j].set_xticks([])
#     ax[i,j].set_yticks([])
#     ax[i,j].set_xticklabels([])
#     ax[i,j].set_xticklabels([])
#     ax[i,j].set_title(col)
#     i += 1
#     if i == 5:
#         i = 0
#         j += 1
# plt.show()

DataViz.plot_dataset(dataset, ['acc_', 'press_', 'gyr_', 'mag_', 'linacc_', 'hr_', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like'], ['line', 'line', 'line', 'line', 'line', 'points','points'])

# Compute the number of milliseconds covered by an instance based on the first two rows
milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds/1000

# Step 1: Let us see whether we have some outliers we would prefer to remove.

# Determine the columns we want to experiment on.
# outlier_columns = ['acc_phone_x', 'light_phone_lux']
outlier_columns = [c for c in dataset.columns if not 'label' in c]

# Create the outlier classes.
OutlierDistr = DistributionBasedOutlierDetection()
OutlierDist = DistanceBasedOutlierDetection()

# #And investigate the approaches for all relevant attributes.
# for col in outlier_columns:
#     # And try out all different approaches. Note that we have done some optimization
#     # of the parameter values for each of the approaches by visual inspection.
#     # dataset = OutlierDistr.chauvenet(dataset, col)
#     # print(col, sum(dataset[col+'_outlier']))
#     # plot = DataViz.plot_binary_outliers(dataset, col, col + '_outlier', ax[i,j])
#
#     dataset = OutlierDistr.mixture_model(dataset, col)
#     DataViz.plot_dataset(dataset, [col, col + '_mixture'], ['exact','exact'], ['line', 'points'])
#     # plot.plot(ax=ax[i,j])
#     # i += 1
#     # if i == 7:
#     #     i = 0
#     #     j = 1
#
#     cols_to_remove = [col + '_outlier', col + '_mixture', 'simple_dist_outlier', 'lof']
#     for to_remove in cols_to_remove:
#         if to_remove in dataset:
#             del dataset[to_remove]


# We take Chauvent's criterion and apply it to all but the label data...

for col in [c for c in dataset.columns if not 'label' in c]:
    print 'Measurement is now: ' , col
    dataset = OutlierDistr.chauvenet(dataset, col)
    print(col, sum(dataset[col+'_outlier']))
    dataset.loc[dataset[col + '_outlier'] == True, col] = np.nan
    del dataset[col + '_outlier']

dataset.to_csv(dataset_path + 'chapter3_final_outliers.csv')
