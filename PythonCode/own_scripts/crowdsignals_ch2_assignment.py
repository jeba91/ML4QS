##############################################################
#                                                            #
#    Mark Hoogendoorn and Burkhardt Funk (2017)              #
#    Machine Learning for the Quantified Self                #
#    Springer                                                #
#    Chapter 2                                               #
#                                                            #
##############################################################


dataset_path = '../csv-participant-one/'
result_dataset_path = './intermediate_datafiles/'

# Import the relevant classes.

from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
import copy
import os
import pandas as pd

data_minute = pd.read_csv(result_dataset_path + "chapter2_result.csv", index_col=0)
data_minute.index = data_minute.index.to_datetime()

data_4hz = pd.read_csv(result_dataset_path + "chapter2_result60000.csv", index_col=0)
data_4hz.index = data_4hz.index.to_datetime()

DataViz = VisualizeDataset()
DataViz.plot_dataset_boxplot(data_minute, ['acc_phone_x','acc_phone_y','acc_phone_z','acc_watch_x','acc_watch_y','acc_watch_z'])
DataViz.plot_dataset(data_minute, ['acc_', 'gyr_', 'hr_watch_rate', 'light_phone_lux', 'mag_', 'press_phone_', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like','like'], ['line', 'line', 'line', 'line', 'line', 'line', 'points', 'points'])
util.print_statistics(data_minute)

DataViz.plot_dataset_boxplot(data_4hz, ['acc_phone_x','acc_phone_y','acc_phone_z','acc_watch_x','acc_watch_y','acc_watch_z'])
DataViz.plot_dataset(data_4hz, ['acc_', 'gyr_', 'hr_watch_rate', 'light_phone_lux', 'mag_', 'press_phone_', 'label'], ['like', 'like', 'like', 'like', 'like', 'like', 'like','like'], ['line', 'line', 'line', 'line', 'line', 'line', 'points', 'points'])
util.print_statistics(data_4hz)

util.print_latex_table_statistics_two_datasets(data_minute, data_4hz)
