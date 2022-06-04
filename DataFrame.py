#Call Library 
import pandas as pd
import matpoltlib.pyplot as plt
# Read In Data
df = pd.read_csv("21.csv",na_values="?")
df.head()
df[df['name'] == 'Drip Coffee'][df['status'] == 'Done']
df.order_reference.mean()
df.groupby('sku').order_reference.mean()
df[df.total_taxes=='0'].order_reference.mean()
df.groupby('total_cost').order_reference.max()
df.groupby('total_cost').order_reference.min()
df.groupby('total_cost').order_reference.agg['count','min','max','mean']
df.groupby('unit_price').mean()

df.groupby('name_localized').mean().plot(kind='bar')

# Groupby - Single Group Single Column
df.groupby(['order_reference'])['sku'].sum()
#Groupby - Multiple Columns
df.groupby(['order_reference'])[['sku','parent_item_sku']].sum()
#Groupby - Multiple Groups
df.groupby(['order_reference','order_status'])[['sku','parent_item_sku']].sum()
#Groupby - Multiple Groups As Columns
df.groupby(['order_reference','order_status'],as_index=False)['sku'].sum()
#Multiple Function
df.groupby(['order_reference'])['sku'].agg(['mean','sum'])
df.groupby(['tax_exclusive_unit_price'])['order_status'].sum()
plt.show()