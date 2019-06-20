##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 4                                               #
#                                                            #
##############################################################

from util.VisualizeDataset import VisualizeDataset
from Chapter4.TemporalAbstraction import NumericalAbstraction
from Chapter4.TemporalAbstraction import CategoricalAbstraction
from Chapter4.FrequencyAbstraction import FourierTransformation
from Chapter4.TextAbstraction import TextAbstraction
import copy
import pandas as pd

# Let us create our visualization class again.
DataViz = VisualizeDataset()

# Read the result from the previous chapter, and make sure the index is of the type datetime.
dataset_path = './intermediate_datafiles/'
try:
    dataset = pd.read_csv(dataset_path + 'chapter4_freq.csv', index_col=0)
except IOError as e:
    print('File not found, try to run previous crowdsignals scripts first!')
    raise e

dataset.index = dataset.index.to_datetime()

# Compute the number of milliseconds covered by an instane based on the first two rows
milliseconds_per_instance = (dataset.index[1] - dataset.index[0]).microseconds/1000

print(dataset.index.max)
# # Chapter 4: Identifying aggregate attributes.
#
# # First we focus on the time domain.
#
# # Set the window sizes to the number of instances representing 5 seconds, 30 seconds and 5 minutes
# window_sizes = [int(float(5000)/milliseconds_per_instance), int(float(20000)/milliseconds_per_instance), int(float(60000)/milliseconds_per_instance)]
#
# NumAbs = NumericalAbstraction()
# dataset_copy = copy.deepcopy(dataset)
# for ws in window_sizes:
#     dataset_copy = NumAbs.abstract_numerical(dataset_copy, ['linacc_Linear Acceleration x (m/s^2)'], ws, 'mean')
#     dataset_copy = NumAbs.abstract_numerical(dataset_copy, ['linacc_Linear Acceleration x (m/s^2)'], ws, 'std')
#
# DataViz.plot_dataset(dataset_copy, ['linacc_Linear Acceleration x (m/s^2)', 'linacc_Linear Acceleration x (m/s^2)_temp_mean', 'linacc_Linear Acceleration x (m/s^2)_temp_std', 'label'], ['exact', 'like', 'like', 'like'], ['line', 'line', 'line', 'points'])
#
# ws = int(float(0.5*60000)/milliseconds_per_instance)
# selected_predictor_cols = [c for c in dataset.columns if not 'label' in c]
# dataset = NumAbs.abstract_numerical(dataset, selected_predictor_cols, ws, 'mean')
# dataset = NumAbs.abstract_numerical(dataset, selected_predictor_cols, ws, 'std')
#
#
# CatAbs = CategoricalAbstraction()
# dataset = CatAbs.abstract_categorical(dataset, ['label'], ['like'], 0.03, int(float(5*60000)/milliseconds_per_instance), 2)
#
#
# # Now we move to the frequency domain, with the same window size.
#
# FreqAbs = FourierTransformation()
# fs = float(1000)/milliseconds_per_instance
#
# periodic_predictor_cols = [c for c in dataset.columns if (not ('label' in c))]
#
# data_table = FreqAbs.abstract_frequency(copy.deepcopy(dataset), ['mag_Magnetic field x (muT)'], int(float(10000)/milliseconds_per_instance), fs)
#
# # Spectral analysis.
#
# DataViz.plot_dataset(data_table, ['mag_Magnetic field x (muT)_max_freq', 'mag_Magnetic field x (muT)_freq_weighted', 'mag_Magnetic field x (muT)_pse', 'label'], ['like', 'like', 'like', 'like'], ['line', 'line', 'line','points'])
#
# dataset = FreqAbs.abstract_frequency(dataset, periodic_predictor_cols, int(float(10000)/milliseconds_per_instance), fs)
#
# # Now we only take a certain percentage of overlap in the windows, otherwise our training examples will be too much alike.

# The percentage of overlap we allow
ws = int(float(4000)/milliseconds_per_instance)
window_overlap = 0.6
skip_points = int((1-window_overlap) * ws)
dataset = dataset.iloc[::skip_points,:]

# Let is create our visualization class again.
DataViz = VisualizeDataset()
DataViz.plot_dataset(dataset, ['acc_', 'press_', 'gyr_', 'mag_', 'linacc_', 'hr_', 'pca_', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like','like', 'like'], ['line', 'line', 'line', 'line', 'line', 'line', 'line', 'points', 'points'])

print(dataset.shape)
dataset.to_csv(dataset_path + 'chapter4_result.csv')

# DataViz.plot_dataset(dataset, ['acc_phone_x', 'gyr_phone_x', 'hr_watch_rate', 'light_phone_lux', 'mag_phone_x', 'press_phone_', 'pca_1', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like','like'], ['line', 'line', 'line', 'line', 'line', 'line', 'line', 'points'])
