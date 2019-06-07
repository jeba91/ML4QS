dataset_path = 'data_phyphox2/'
result_dataset_path = 'own_datafiles/'
figures_save_path = 'figures/'

# Import the relevant classes.

from PythonCode.Chapter2.CreateDataset import CreateDataset
from PythonCode.util.VisualizeDataset import VisualizeDataset
from PythonCode.util import util
import pandas as pd
import copy
import os


if not os.path.exists(result_dataset_path):
    print('Creating result directory: ' + result_dataset_path)
    os.makedirs(result_dataset_path)

prefix1 = "acc_"
file1 = "Accelerometer.csv"
cols1 = ["X (m/s^2)","Y (m/s^2)","Z (m/s^2)","label"]
cols_pre1 = [prefix1+x for x in cols1]

prefix2 = "bar_"
file2 = "Barometer.csv"
cols2 = ["X (hPa)"]
cols_pre2 = [prefix2+x for x in cols2]

prefix3 = "gyr_"
file3 = "Gyroscope.csv"
cols3 = ["X (rad/s)","Y (rad/s)","Z (rad/s)"]
cols_pre3 = [prefix3+x for x in cols3]

DataSet = CreateDataset(dataset_path, 60000)

DataSet.add_numerical_dataset(file1, 'Time (s)', cols1, 'avg', prefix1)
DataSet.add_numerical_dataset(file2, 'Time (s)', cols2, 'avg', prefix2)
DataSet.add_numerical_dataset(file3, 'Time (s)', cols3, 'avg', prefix3)


dataset = DataSet.data_table

DataViz = VisualizeDataset()
fig1 = DataViz.plot_dataset_boxplot(dataset, cols_pre3 + cols_pre2 + cols_pre1)
fig1.savefig(figures_save_path+"box")
fig2 = DataViz.plot_dataset(dataset, cols_pre3 + cols_pre2 + cols_pre1,['like', 'like', 'like','like', 'like', 'like','like','like'],['line', 'line', 'line','line', 'line', 'line','line','points'])
fig2.savefig(figures_save_path+"plot")
