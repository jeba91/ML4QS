##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 3                                               #
#                                                            #
##############################################################

from util.VisualizeDataset import VisualizeDataset
from Chapter3.DataTransformation import LowPassFilter
from Chapter3.DataTransformation import PrincipalComponentAnalysis
from Chapter3.ImputationMissingValues import ImputationMissingValues
from Chapter3.KalmanFilters import KalmanFilters
import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Let is create our visualization class again.
DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sure the index is of the type datetime.
dataset_path = './intermediate_datafiles/'
dataset = pd.read_csv(dataset_path + 'chapter3_result_outliers.csv', index_col=0)
dataset.index = dataset.index.to_datetime()

# Computer the number of milliseconds covered by an instane based on the first two rows
milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds/1000

MisVal = ImputationMissingValues()

imputed_mean_dataset = MisVal.impute_mean(copy.deepcopy(dataset), 'hr_watch_rate')
imputed_median_dataset = MisVal.impute_median(copy.deepcopy(dataset), 'hr_watch_rate')
imputed_interpolation_dataset = MisVal.impute_interpolate(copy.deepcopy(dataset), 'hr_watch_rate')

dataset2 = copy.deepcopy(dataset)

dataset2['gyr_phone_x'] = MisVal.impute_mean(copy.deepcopy(dataset2), 'gyr_phone_x')
dataset2['gyr_phone_y'] = MisVal.impute_mean(copy.deepcopy(dataset2), 'gyr_phone_y')
dataset2['gyr_phone_z'] = MisVal.impute_mean(copy.deepcopy(dataset2), 'gyr_phone_z')


X = dataset2[['acc_phone_x','acc_phone_y','acc_phone_z','gyr_phone_x','gyr_phone_y','gyr_phone_z']].loc[dataset2['hr_watch_rate'].isnull()==False]
X_pred = dataset2[['acc_phone_x','acc_phone_y','acc_phone_z','gyr_phone_x','gyr_phone_y','gyr_phone_z']].loc[dataset2['hr_watch_rate'].isnull()==True]
y = dataset2['hr_watch_rate'].loc[dataset2['hr_watch_rate'].isnull()==False]

predictor = LinearRegression()

predictor.fit(X=X, y=y)
y_pred = predictor.predict(X=X_pred)

dataset2['hr_watch_rate'].loc[dataset2['hr_watch_rate'].isnull()==True] = y_pred

DataViz.plot_imputed_values(dataset, ['original', 'model', 'interpolation'], 'hr_watch_rate', dataset2['hr_watch_rate'], imputed_interpolation_dataset['hr_watch_rate'])

# scores = []
# kfold = KFold(n_splits=3, shuffle=True, random_state=42)
# for i, (train, test) in enumerate(kfold.split(X, y)):
#     model.fit(X.iloc[train,:], y.iloc[train,:])
#     score = model.score(X.iloc[test,:], y.iloc[test,:])
#     scores.append(score)
# print(scores)
