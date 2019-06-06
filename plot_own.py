import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("own_data.csv", index_col=0)

good_cols = ['Time (s)','X (hPa)','Latitude (°)','Longitude (°)','Height (m)','Velocity (m/s)', 'Direction (°)','Horizontal Accuracy (m)','Vertical Accuracy (°)','X (m/s^2)', 'Y (m/s^2)','Z (m/s^2)','X (rad/s)', 'Y (rad/s)', 'Z (rad/s)','X (µT)','Y (µT)','Z (µT)',]

drop_cols = ['sensor','Time (s).1','sensor.1','Time (s).2','sensor.2','Time (s).3','sensor.3','Time (s).4','sensor.4','activity']

df1 = df.drop(columns=drop_cols)

df1.loc[df['activity'] == "walking2"].plot(subplots=True, layout=(4,5), xticks=df.index)
plt.show()
