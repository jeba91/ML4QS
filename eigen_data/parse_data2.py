import os
import pandas as pd

df = pd.DataFrame()

current_map = "data_phyphox1/"
save_map = "data_phyphox2/"

for x in os.listdir(current_map):
    df = pd.DataFrame()
    for i,y in enumerate(sorted(os.listdir(current_map + "/" + x))):
        data = pd.read_csv(current_map + "/" + x + "/" + y)
        data["label"] = i
        df = pd.concat([df,data])
    df.to_csv(save_map + "/" + x + ".csv")
