#find the amount of charge total for this location
import pandas as pd
import numpy as np

df = pd.read_csv("concatenatedFieldData.csv")
df.head()
d1 = df[(df["sig_name"]=="percent_chg") & (df["feature"]=='CycleLastValue')].reset_index()
d2 = df[(df["sig_name"]=="percent_chg") & (df["feature"]=='CycleFirstValue')].reset_index()

dt = d1.copy()
dt['charge_value'] = d1['value'] - d2['value']
dx = pd.pivot_table(dt,index=["scin"],values=["charge_value"],aggfunc=np.sum)
dx=dx.sort_values(by=['charge_value'],ascending=False)

print(dx)
export_csv = dx.to_csv (r'totalChargeField.csv', index = ["scin"], header=True)
