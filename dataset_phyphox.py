dataset_path = 'data_phyphox2/'
result_dataset_path = 'own_datafiles/'

# Import the relevant classes.

from PythonCode.Chapter2.CreateDataset import CreateDataset
from PythonCode.util.VisualizeDataset import VisualizeDataset
from PythonCode.util import util
import copy
import os


if not os.path.exists(result_dataset_path):
    print('Creating result directory: ' + result_dataset_path)
    os.makedirs(result_dataset_path)

granularities = [60000, 250]
datasets = []

DataSet = CreateDataset(dataset_path, 1000)
DataSet.add_numerical_dataset('biking.csv', 'Time (s)', ["X (m/s^2)","Y (m/s^2)","Z (m/s^2)"], 'avg', 'biking_')

dataset = DataSet.data_table


DataViz = VisualizeDataset()
DataViz.plot_dataset_boxplot(dataset, ['biking_X (m/s^2)','biking_Y (m/s^2)','biking_Z (m/s^2)'])
DataViz.plot_dataset(dataset, ['biking_X (m/s^2)','biking_Y (m/s^2)','biking_Z (m/s^2)'],['like', 'like', 'like'],['line', 'line', 'line'])
