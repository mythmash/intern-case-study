#using concatenated field data, counts occurrences of usage at each location, sorts by number of uses
import pandas as pd
import numpy as np

df = pd.read_csv("concatenatedFieldData.csv")
df.head()

df = df[(df["sig_name"]=="percent_chg") & (df["feature"]=='CycleFirstValue')].reset_index()
df['count'] = df.groupby('scin')['scin'].transform('count')
df['count'] = df['count']
df=df.sort_values(by=['count'],ascending=False)
#because there are many copies of the same site made, delete the duplicates
df=df.drop_duplicates(subset='scin', keep="last")
df=df.reset_index()

del df['Unnamed: 0'], df['Unnamed: 0.1'], df['level_0'], df['sig_name'], df['feature'], df['value'], df['index'], df['start_epoch_ms'], df['end_epoch_ms']

print(df)
export_csv = df.to_csv (r'numUsesBySiteField.csv', index = ["scin"], header=True)