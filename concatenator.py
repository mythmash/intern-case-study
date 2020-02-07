#concatenates all field data files

import pandas as pd
import numpy as np

arr=["field_data/Feb-data-2019.csv","field_data/March-data-2019.csv","field_data/April-data-2019.csv","field_data/May-data-2019.csv","field_data/June-data-2019.csv","field_data/July-data-2019.csv","field_data/Aug-data-2019.csv","field_data/Sept-data-2019.csv","field_data/Nov-data-2019.csv","field_data/Dec-data-2019.csv"]
res=pd.read_csv("field_data/Jan-data-2019.csv")
res.head() 
#res.drop(columns=['start_epoch_ms','end_epoch_ms'])
#del res['start_epoch_ms']
#del res['end_epoch_ms']
del res['event_date']
del res['cycle_name']

#iterate through the months
for file_name in arr:     
    print("running")
    df = pd.read_csv(file_name)
    df.head() 
    #df.drop(columns=['start_epoch_ms','end_epoch_ms','event_date'])
    # del df['start_epoch_ms']
    # del df['end_epoch_ms']
    del df['event_date']
    del df['cycle_name']
    res = pd.concat([res, df], sort=False)

export_csv = res.to_csv (r'concatenatedFieldData.csv', index = ["scin"], header=True)
