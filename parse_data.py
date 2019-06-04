import os
import pandas as pd

df = pd.DataFrame()

for x in os.listdir("data_phyphox"):
    df_temp = pd.DataFrame()
    for y in os.listdir("data_phyphox/" + x):
        print("data_phyphox/"+x+"/"+y)
        data = pd.read_csv("data_phyphox/"+x+"/"+y)
        df_temp = pd.concat([df_temp,data],1)
    print(df_temp.shape)
    df = df.append(df_temp)

print(df)

df.to_csv("own_data.csv")
