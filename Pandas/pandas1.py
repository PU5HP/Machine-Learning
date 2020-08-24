import numpy as np
import pandas as pd

#pandas module is used to work with the tabular data
#creating a data frame ===> representing inthe tabular form

create_table = {
    'mansi'  :np.random.randint(1,100,5),
    'madhav' : np.random.randint(1,100,5),
    'pushp' : np.random.randint(1,100,5),
}
print(create_table)

#representation in tabular form
df = pd.DataFrame(create_table)
print(df)

#printing all the columns
print(df.columns)

#printing some data with use of the head 
print(df.head(n=2))

#creating a csv file
df.to_csv('marks.csv')

my_data = pd.read_csv('marks.csv')
my_data = my_data.drop(columns=['Unnamed: 0'])
print(my_data)
