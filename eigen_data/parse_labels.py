import os
import pandas as pd

df = pd.DataFrame()


epoch_time = 1559653200000000000

current_map = "data_phyphox/"
save_map = "data_phyphox1/"

dir_list = os.listdir("data_phyphox/")
dir_list2 = os.listdir("data_phyphox/biking/")

# interval_label,smartphone,On Table,1454956132985999872.000,08/02/2016 10:28:52,1454956366574000128.000,08/02/2016 10:32:46

for x in os.listdir(current_map):
    for i,y in enumerate(os.listdir(current_map + "/" + x)):
        data = pd.read_csv(current_map + "/" + x + "/" + y)
        max = round(data["Time (s)"].max())+1
        data["Time (s)"] = (data["Time (s)"].apply(lambda x: (x*1000000000)+epoch_time))
        # data.to_csv(save_map + y.split('.')[0] + "/" + x + "_" + y)

    print(x,epoch_time,pd.to_datetime(epoch_time),(epoch_time+max*1000000000),pd.to_datetime(epoch_time+max*1000000000))
    epoch_time += max*1000000000
    print(pd.to_datetime(epoch_time))

    # print(epoch_time)
