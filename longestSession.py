#finds the longest session (by placing it first after sorting) and the average time of all sessions
import pandas as pd
import numpy as np

df = pd.read_csv("concatenatedFieldData.csv")
df.head()

d2 = df[(df["sig_name"]=="percent_chg") & (df["feature"]=='CycleFirstValue')].reset_index()

dt = d2.copy()
dt['time_used'] = d2['end_epoch_ms'] - d2['start_epoch_ms']
dt=dt.reset_index()
del dt['Unnamed: 0'], dt['Unnamed: 0.1'], dt['index'],dt['sig_name'], dt['feature'], dt['value'], dt['start_epoch_ms'], dt['end_epoch_ms'], dt['level_0']

dt=dt.sort_values(by=['time_used'],ascending=False)

avg=dt["time_used"].mean
print(avg)
export_csv = dt.to_csv (r'sortedUsageTimes.csv', index = ["scin"], header=True)