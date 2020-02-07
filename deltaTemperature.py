#find the largest temperature difference for each charging session and sort by difference
import pandas as pd

df = pd.read_csv("concatenatedFieldData.csv")
df.head()

#split into separate tables for CycleFirstValue, CycleLastValue, and Min
dfr = df[(df["sig_name"]=="handle_temp") & (df["feature"]=='CycleLastValue')].reset_index()
dsc = df[(df["sig_name"]=="handle_temp") & (df["feature"]=='CycleFirstValue')].reset_index()
dmin = df[(df["sig_name"]=="handle_temp") & (df["feature"]=='Min')].reset_index()

del dsc['scin'], dmin['scin']

dsc=dsc.rename(columns={'value':'second'})
dmin=dmin.rename(columns={'value':'third'})
dt = dfr.copy()
dt = pd.concat([dfr, dsc], axis=1)
dt = pd.concat([dt, dmin], axis=1)
v = dt[['value', 'second', 'third']].values
#find and keep the maximum difference (compare CycleFirst-Min and CycleLast-Min)
dt['dT'] = v.max(1) - v.min(1)

del dt['Unnamed: 0'], dt['Unnamed: 0.1'], dt['index']
dt=pd.pivot_table(dt,index=["scin"],values=["dT"])
dt=dt.sort_values(by=['dT'],ascending=False)
#print(dt)
export_csv = dt.to_csv (r'deltaTemperatureField.csv', index = ["scin"], header=True)
