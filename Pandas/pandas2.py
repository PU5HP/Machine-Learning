import numpy as np
import pandas as pd

create_table_2 = {
    'ravi':[1,32,3,44,5],
    'paras':[13,2,32,4,35],
    'pushp':[1,23,3,43,5],
}

df = pd.DataFrame(create_table_2)
print(df)

#describing the table
print(df.describe())

#access the elements from the last 
print(df.tail(n=3))

#accessing the specific elements inthe table
#rows
print(df.iloc[3])
print(df.iloc[3][0])

# accessing more columns and rows
idx = [df.columns.get_loc('ravi'),df.columns.get_loc('pushp')]
print(idx)
print(df.iloc[3,idx])
print(df.iloc[:3,[1,2]])

#sort
print(df.sort_values(by=['pushp','ravi']))

#creating a numpy array 
array_np = df.values
print(type(array_np))

#creating a df from a numpy array
new_df = pd.DataFrame(array_np,dtype='int32',columns=['physics','chemistry','maths'])
print(new_df)

new_df.to_csv('pcm.csv',index=False)



