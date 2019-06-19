##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 8                                               #
#                                                            #
##############################################################

from util.VisualizeDataset import VisualizeDataset
from Chapter7.PrepareDatasetForLearning import PrepareDatasetForLearning
from Chapter7.Evaluation import RegressionEvaluation
from Chapter8.LearningAlgorithmsTemporal import TemporalClassificationAlgorithms
from Chapter8.LearningAlgorithmsTemporal import TemporalRegressionAlgorithms
from statsmodels.tsa.stattools import adfuller
from pandas.tools.plotting import autocorrelation_plot

import copy
import pandas as pd
from util import util
import matplotlib.pyplot as plot
import numpy as np
from sklearn.model_selection import train_test_split


# Of course we repeat some stuff from Chapter 3, namely to load the dataset

DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sure the index is of the type datetime.
dataset_path = './intermediate_datafiles/'

try:
    dataset = pd.read_csv(dataset_path + 'chapter5_result.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e

dataset.index = dataset.index.to_datetime()

# Let us consider our second task, namely the prediction of the heart rate. We consider this as a temporal task.

prepare = PrepareDatasetForLearning()

train_X, test_X, train_y, test_y = prepare.split_single_dataset_regression_by_time(dataset, 'hr_watch_rate', '2016-02-08 18:29:56',
#                                                                                   '2016-02-08 18:29:58','2016-02-08 18:29:59')
                                                                                   '2016-02-08 19:34:07', '2016-02-08 20:07:50')

print 'Training set length is: ', len(train_X.index)
print 'Test set length is: ', len(test_X.index)

# Select subsets of the features that we will consider:

print 'Training set length is: ', len(train_X.index)
print 'Test set length is: ', len(test_X.index)

# Select subsets of the features that we will consider:

basic_features = ['acc_phone_x','acc_phone_y','acc_phone_z','acc_watch_x','acc_watch_y','acc_watch_z','gyr_phone_x','gyr_phone_y','gyr_phone_z','gyr_watch_x','gyr_watch_y','gyr_watch_z',
                  'labelOnTable','labelSitting','labelWashingHands','labelWalking','labelStanding','labelDriving','labelEating','labelRunning',
                  'light_phone_lux','mag_phone_x','mag_phone_y','mag_phone_z','mag_watch_x','mag_watch_y','mag_watch_z','press_phone_pressure']

pca_features = ['pca_1','pca_2','pca_3','pca_4','pca_5','pca_6','pca_7']
time_features = [name for name in dataset.columns if ('temp_' in name and not 'hr_watch' in name)]
freq_features = [name for name in dataset.columns if (('_freq' in name) or ('_pse' in name))]
print '#basic features: ', len(basic_features)
print '#PCA features: ', len(pca_features)
print '#time features: ', len(time_features)
print '#frequency features: ', len(freq_features)
cluster_features = ['cluster']
print '#cluster features: ', len(cluster_features)
features_after_chapter_3 = list(set().union(basic_features, pca_features))
features_after_chapter_4 = list(set().union(basic_features, pca_features, time_features, freq_features))
features_after_chapter_5 = list(set().union(basic_features, pca_features, time_features, freq_features, cluster_features))

selected_features = ['temp_pattern_labelOnTable','labelOnTable', 'temp_pattern_labelOnTable(b)labelOnTable', 'cluster',
                     'pca_1_temp_mean_ws_120','pca_2_temp_mean_ws_120','pca_2','acc_watch_y_temp_mean_ws_120','gyr_watch_y_pse',
                     'gyr_watch_x_pse']
possible_feature_sets = [basic_features, features_after_chapter_3, features_after_chapter_4, features_after_chapter_5, selected_features]
feature_names = ['initial set', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Selected features']
import math
import matplotlib.pyplot as plt
print(dataset.shape)
dataset['acc_phone_total'] = dataset['acc_phone_x']**2 + dataset['acc_phone_y']**2 + dataset['acc_phone_z']**2
dataset['acc_phone_total'] = dataset['acc_phone_total'].apply(lambda x : math.sqrt(x))

dataset['acc_watch_total'] = dataset['acc_watch_x']**2 + dataset['acc_watch_y']**2 + dataset['acc_watch_z']**2
dataset['acc_watch_total'] = dataset['acc_watch_total'].apply(lambda x : math.sqrt(x))

dataset['gyr_phone_total'] = dataset['gyr_phone_x']**2 + dataset['gyr_phone_y']**2 + dataset['gyr_phone_z']**2
dataset['gyr_phone_total'] = dataset['gyr_phone_total'].apply(lambda x : math.sqrt(x))

dataset['gyr_watch_total'] = dataset['gyr_watch_x']**2 + dataset['gyr_watch_y']**2 + dataset['gyr_watch_z']**2
dataset['gyr_watch_total'] = dataset['gyr_watch_total'].apply(lambda x : math.sqrt(x))

dataset['mag_phone_total'] = dataset['mag_phone_x']**2 + dataset['mag_phone_y']**2 + dataset['mag_phone_z']**2
dataset['mag_phone_total'] = dataset['mag_phone_total'].apply(lambda x : math.sqrt(x))

dataset['mag_watch_total'] = dataset['mag_watch_x']**2 + dataset['mag_watch_y']**2 + dataset['mag_watch_z']**2
dataset['mag_watch_total'] = dataset['mag_watch_total'].apply(lambda x : math.sqrt(x))

dataset['acc_phone_total']

dataset.to_csv(dataset_path + 'chapter8_result.csv')
