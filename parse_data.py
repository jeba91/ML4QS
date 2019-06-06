import os
import pandas as pd

df = pd.DataFrame()


epoch_time = 1559653200000000000

current_map = "data_phyphox/"
save_map = "data_phyphox1/"

dir_list = os.listdir("data_phyphox/")
dir_list2 = os.listdir("data_phyphox/biking/")


for x in os.listdir(current_map):
    for i,y in enumerate(os.listdir(current_map + "/" + x)):
        data = pd.read_csv(current_map + "/" + x + "/" + y)
        data["Time (s)"] = (data["Time (s)"].apply(lambda x: (x*1000000000)+epoch_time))
        data["label"] = x
        data.to_csv(save_map + y.split('.')[0] + "/" + x + "_" + y)
    epoch_time += (data["Time (s)"].max()*1000000000)
