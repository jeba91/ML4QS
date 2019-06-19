import os
import pandas as pd
import math

df = pd.DataFrame()


epoch_time = 1559653200000000000

current_map = "data_final/"
save_map = "data_final1/"


for x in sorted(os.listdir(current_map)):
    maxi = 0
    for i,y in enumerate(sorted(os.listdir(current_map + "/" + x))):
        data = pd.read_csv(current_map + "/" + x + "/" + y)
        maxi = max(round(data["Time (s)"].max())+1, maxi)
        data["Time (s)"] = (data["Time (s)"].apply(lambda x: (x*1000000000)+epoch_time))
        save1 = y.split('.')[0]
        if not os.path.exists(save_map + save1.replace(" ", "")):
            os.mkdir(save_map + save1.replace(" ", ""))
        data.to_csv(save_map + save1.replace(" ", "") + "/" + x + "_" + y.replace(" ", ""))
    epoch_time += maxi*1000000000
    # print(epoch_time)
