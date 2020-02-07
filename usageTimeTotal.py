#find the amount of time that each location was in use
import pandas as pd
import numpy as np

df = pd.read_csv("concatenatedFieldData.csv")
df.head()

d2 = df[(df["sig_name"]=="percent_chg") & (df["feature"]=='CycleFirstValue')].reset_index()

dt = d2.copy()
dt['time_used'] = d2['end_epoch_ms'] - d2['start_epoch_ms']
dt=dt.reset_index()
del dt['Unnamed: 0'], dt['Unnamed: 0.1'], dt['index'],dt['sig_name'], dt['feature'], dt['value'], dt['start_epoch_ms'], dt['end_epoch_ms'], dt['level_0']
dt = pd.pivot_table(dt,index=["scin"],values=["time_used"],aggfunc=np.sum)
dt=dt.sort_values(by=['time_used'],ascending=False)


print(dt)
export_csv = dt.to_csv (r'totalUsageTimeField.csv', index = ["scin"], header=True)