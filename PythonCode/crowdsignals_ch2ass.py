dataset_path = 'data_phyphox2/'
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
cols1 = ["X (m/s^2)","Y (m/s^2)","Z (m/s^2)"]
cols_pre1 = [prefix1+x for x in cols1]

prefix2 = "bar_"
file2 = "Barometer.csv"
cols2 = ["X (hPa)"]
cols_pre2 = [prefix2+x for x in cols2]

prefix3 = "gyr_"
file3 = "Gyroscope.csv"
cols3 = ["X (rad/s)","Y (rad/s)","Z (rad/s)"]
cols_pre3 = [prefix3+x for x in cols3]

prefix4 = "mag_"
file4 = "Magnetometer.csv"
cols4 = ["X (muT)","Y (muT)","Z (muT)"]
cols_pre4 = [prefix4+x for x in cols4]

prefix5 = "loc_"
file5 = "Location.csv"
cols5 = ["Latitude (degree)","Longitude (degree)","Height (m)","Velocity (m/s)","Direction (degree)","Horizontal Accuracy (m)","Vertical Accuracy (degree)"]
cols_pre5 = [prefix5+x for x in cols5]

# DataSet = CreateDataset(dataset_path, 60000)
DataSet = CreateDataset(dataset_path, 250)

DataSet.add_numerical_dataset(file1, 'Time (s)', cols1, 'avg', prefix1)
DataSet.add_numerical_dataset(file2, 'Time (s)', cols2, 'avg', prefix2)
DataSet.add_numerical_dataset(file3, 'Time (s)', cols3, 'avg', prefix3)
DataSet.add_numerical_dataset(file4, 'Time (s)', cols4, 'avg', prefix4)
DataSet.add_numerical_dataset(file5, 'Time (s)', cols5, 'avg', prefix5)

DataSet.add_event_dataset('labels.csv', 'label_start', 'label_end', 'label', 'binary')

dataset = DataSet.data_table

print(dataset.columns)
print(cols_pre1)

# fig, ax = plt.subplots(7,1, sharex=True)
#
# dataset.reset_index().plot(x='index',y=cols_pre1[:-1], title=file1, ax=ax[0],legend=False)
# ax[0].legend(cols1,loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 6})
# dataset.reset_index().plot(x='index',y=cols_pre2[:-1], title=file2, ax=ax[1],legend=False)
# ax[1].legend(cols2,loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 6})
# dataset.reset_index().plot(x='index',y=cols_pre3[:-1], title=file3, ax=ax[2],legend=False)
# ax[2].legend(cols3,loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 6})
# dataset.reset_index().plot(x='index',y=cols_pre4[:-1], title=file4, ax=ax[3],legend=False)
# ax[3].legend(cols4,loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 6})
# dataset.reset_index().plot(x='index',y=cols_pre5[4], title="Velocity (m/s)", ax=ax[4],legend=False)
# dataset.reset_index().plot(x='index',y=cols_pre5[3], title="Height (m)", ax=ax[5],legend=False)
#
# dataset[cols_pre1[-1]] = dataset[cols_pre1[-1]].loc[dataset[cols_pre1[-1]] == 1]
# dataset[cols_pre2[-1]] = dataset[cols_pre2[-1]].loc[dataset[cols_pre2[-1]] == 2]
# dataset[cols_pre3[-1]] = dataset[cols_pre3[-1]].loc[dataset[cols_pre3[-1]] == 3]
# dataset[cols_pre4[-1]] = dataset[cols_pre4[-1]].loc[dataset[cols_pre4[-1]] == 4]
# dataset[cols_pre5[-1]] = dataset[cols_pre5[-1]].loc[dataset[cols_pre5[-1]] == 5]
#
# dataset.reset_index().plot(x='index',y=cols_pre1[-1], style="x", ax=ax[6], c="red")
# dataset.reset_index().plot(x='index',y=cols_pre2[-1], style="x", ax=ax[6], c="blue")
# dataset.reset_index().plot(x='index',y=cols_pre3[-1], style="x", ax=ax[6], c="green")
# dataset.reset_index().plot(x='index',y=cols_pre4[-1], style="x", ax=ax[6], c="yellow")
# dataset.reset_index().plot(x='index',y=cols_pre5[-1], style="x", title="Activities", ax=ax[6], c="black")
#
# ax[6].legend(["biking","climbing stairs","nothing","walking","train"],loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 6})
# ax[6].set_ylim(0,6)
# plt.show()


# DataViz = VisualizeDataset()
# fig1 = DataViz.plot_dataset_boxplot(dataset, cols_pre4 + cols_pre3 + cols_pre2 + cols_pre1)
# # fig1.savefig(figures_save_path+"box")
# fig2 = DataViz.plot_dataset(dataset, cols_pre3 + cols_pre2 + cols_pre1,['like', 'like', 'like','like', 'like', 'like','like','like'],['line', 'line', 'line','line', 'line', 'line','line','points'])
# # fig2.savefig(figures_save_path+"plot")
#
# print(dataset.columns)

dataset.to_csv(result_dataset_path + "chapter2_own.csv")
