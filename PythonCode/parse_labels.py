import os
import pandas as pd
import numpy as np

df = pd.DataFrame()

# python parse_labels.py > data_final2/labels.csv

current_map = "data_final1/Accelerometer"
save_map = "data_final1/"

# interval_label,smartphone,On Table,1454956132985999872.000,08/02/2016 10:28:52,1454956366574000128.000,08/02/2016 10:32:46
print('sensor_type,device_type,label,label_start,label_start_datetime,label_end,label_end_datetime')
for i,x in enumerate(sorted(os.listdir(current_map))):
    data = pd.read_csv(current_map + "/" + x)
    max = np.int64(round(data["Time (s)"].max())+1)
    min = np.int64(round(data["Time (s)"].min()))
    x = x.split('_')[1]
    d1 = pd.to_datetime(min).strftime('%Y %m %d %H:%M.%S')
    d2 = pd.to_datetime(max).strftime('%Y %m %d %H:%M.%S')
    labelrow = ['interval_label', 'smartphone', str(x) , str(min), d1, str(max), d2]
    print((','.join(labelrow)))
