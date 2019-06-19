import pandas as pd
import datetime
import matplotlib.pyplot as plt

heartdf = pd.read_csv('heartdf.csv', index_col=0)

heartdf['Time'] = pd.to_datetime(heartdf['Time'])
heartdf2 = pd.DataFrame()

dates_j = ['18/06/2019 12:31:20', '18/06/2019 12:36:26']
dates = ['18/06/2019 12:08:47', '18/06/2019 12:24:39', '18/06/2019 12:16:07', '18/06/2019 11:47:06', '18/06/2019 11:39:37',
         '18/06/2019 11:58:31', '18/06/2019 11:31:47', '18/06/2019 11:09:51', '18/06/2019 10:51:10', '18/06/2019 11:02:22',
         '18/06/2019 11:21:24']

date_dt1 = datetime.datetime.strptime(dates_j[0], '%d/%m/%Y %H:%M:%S')
criteria_1 = heartdf['Time'] >= date_dt1
criteria_2 = heartdf['Time'] <= date_dt1 + datetime.timedelta(seconds=120)
criteria_all = criteria_1 & criteria_2
heartdf2 = heartdf2.append(heartdf.loc[criteria_all])

date_dt1 = datetime.datetime.strptime(dates_j[1], '%d/%m/%Y %H:%M:%S')
criteria_1 = heartdf['Time'] >= date_dt1
criteria_2 = heartdf['Time'] <= date_dt1 + datetime.timedelta(seconds=180)
criteria_all = criteria_1 & criteria_2
heartdf2 = heartdf2.append(heartdf.loc[criteria_all])

for dat in dates:
    date_dt1 = datetime.datetime.strptime(dat, '%d/%m/%Y %H:%M:%S')
    criteria_1 = heartdf['Time'] >= date_dt1
    criteria_2 = heartdf['Time'] <= date_dt1 + datetime.timedelta(seconds=300)
    criteria_all = criteria_1 & criteria_2
    heartdf2 = heartdf2.append(heartdf.loc[criteria_all])

heartdf2['diff time'] = heartdf2['Time'].diff()
heartdf2['diff time'] = heartdf2['diff time'].apply(lambda x: x.value)

for i,t in heartdf2['diff time'].iteritems():
    if t > 16000000000 or t < 0:
        print(t)
        heartdf2['diff time'][i] = 15000000000

epoch_time = 1559653200000000000
heartdf2['diff time'][0] = 0
heartdf2 = heartdf2.reset_index()
heartdf2['time'] = heartdf2['diff time']
for i,t in heartdf2['diff time'].iteritems():
    epoch_time += t
    heartdf2['time'][i] = epoch_time

heartdf2 = heartdf2.set_index('time')
heartdf2.index = heartdf2.index.to_datetime()

heartdf['Time (s)'] = heartdf['index']
heartdf[['Time (s)','Heart Rate']].to_csv('heartdf2.csv')
