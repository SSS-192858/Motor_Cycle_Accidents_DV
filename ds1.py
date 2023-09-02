import pandas as pd;
import numpy as np;
df = pd.read_csv("Dataset1.csv")
print(df)

column_headers = list(df.columns.values)
print(df.describe())
print(column_headers)