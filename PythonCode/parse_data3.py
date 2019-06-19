dataset_path = 'data_final2/'
result_dataset_path = 'intermediate_datafiles/'
figures_save_path = 'figures/'

# Import the relevant classes.

from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
import pandas as pd
import copy
import os
import matplotlib.pyplot as plt


if not os.path.exists(result_dataset_path):
    print('Creating result directory: ' + result_dataset_path)
    os.makedirs(result_dataset_path)

prefix1 = "acc_"
file1 = "Accelerometer.csv"
cols1 = ["Acceleration x (m/s^2)","Acceleration y (m/s^2)","Acceleration z (m/s^2)"]
cols_pre1 = [prefix1+x for x in cols1]

prefix2 = "press_"
file2 = "Pressure.csv"
cols2 = ["Pressure (hPa)"]
cols_pre2 = [prefix2+x for x in cols2]

prefix3 = "gyr_"
file3 = "Gyroscope.csv"
cols3 = ["Gyroscope x (rad/s)","Gyroscope y (rad/s)","Gyroscope z (rad/s)"]
cols_pre3 = [prefix3+x for x in cols3]

prefix4 = "mag_"
file4 = "Magnetometer.csv"
cols4 = ["Magnetic field x (muT)","Magnetic field y (muT)","Magnetic field z (muT)"]
cols_pre4 = [prefix4+x for x in cols4]

prefix5 = "linacc_"
file5 = "LinearAcceleration.csv"
cols5 = ["Linear Acceleration x (m/s^2)","Linear Acceleration y (m/s^2)","Linear Acceleration z (m/s^2)"]
cols_pre5 = [prefix5+x for x in cols5]

prefix6 = "hr_"
file6 = "heartdf2.csv"
cols6 = ["Heart Rate"]
cols_pre6 = [prefix6+x for x in cols5]

# DataSet = CreateDataset(dataset_path, 60000)
DataSet = CreateDataset(dataset_path, 500)

DataSet.add_numerical_dataset(file1, 'Time (s)', cols1, 'avg', prefix1)
DataSet.add_numerical_dataset(file2, 'Time (s)', cols2, 'avg', prefix2)
DataSet.add_numerical_dataset(file3, 'Time (s)', cols3, 'avg', prefix3)
DataSet.add_numerical_dataset(file4, 'Time (s)', cols4, 'avg', prefix4)
DataSet.add_numerical_dataset(file5, 'Time (s)', cols5, 'avg', prefix5)
DataSet.add_numerical_dataset(file6, 'Time (s)', cols6, 'avg', prefix6)

DataSet.add_event_dataset('labels.csv', 'label_start', 'label_end', 'label', 'binary')

dataset = DataSet.data_table

dataset.to_csv(result_dataset_path + "chapter2_final2hz.csv")
