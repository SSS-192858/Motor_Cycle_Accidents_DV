import pandas as pd;
import numpy as np;
from datetime import datetime

df = pd.read_csv("./data.csv")

df['CRASH DATE'] = df['CRASH DATE'].apply(lambda _: datetime.strptime(_,"%m/%d/%Y"))
# print(df['CRASH DATE'].dtypes)
df.sort_values(by=['CRASH DATE'],inplace=True)
df1 = df[df['CRASH DATE']<"2014-01-01"]
df = df[df['CRASH DATE']>="2014-01-01"]
df2=df[df['CRASH DATE']<"2016-01-01"]
df = df[df['CRASH DATE']>="2016-01-01"]
df3 = df[df['CRASH DATE']<"2018-01-01"]
df=df[df['CRASH DATE']>="2018-01-01"]
df4=df[df['CRASH DATE']<"2020-01-01"]
df=df[df['CRASH DATE']>="2020-01-01"]
print(df1.shape)
print(df2.shape)
print(df3.shape)
print(df4.shape)
print(df.shape)

df1.to_csv("Dataset1.csv")
df2.to_csv("Dataset2.csv")
df3.to_csv("Dataset3.csv")
df4.to_csv("Dataset4.csv")
df.to_csv("Dataset5.csv")

