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

prefix = "bar_"
file = "Barometer.csv"
cols = ["X (hPa)"]
cols_pre = [prefix+x for x in cols]

DataSet = CreateDataset(dataset_path, 6000)
DataSet.add_numerical_dataset(file, 'Time (s)', cols, 'avg', prefix)

dataset = DataSet.data_table

DataViz = VisualizeDataset()
fig1 = DataViz.plot_dataset_boxplot(dataset, cols_pre)
fig1.savefig(figures_save_path+prefix+"box")
fig2 = DataViz.plot_dataset(dataset, cols_pre,['like'],['line'])
fig2.savefig(figures_save_path+prefix+"plot")
