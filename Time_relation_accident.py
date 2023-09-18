import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import time
from cleanupFile import cleanUp, groupingDictionary_common, custom_acc_type
plt.rcParams['figure.figsize'] = (30,15)
plt.rcParams.update({'font.size': 15})

df = pd.read_csv("./Dataset5.csv")
cleanUp(df)

time1 = time(6,00,00)
time2 = time(12,00,00)
time3 = time(16,30,00)
time4 = time(22,00,00)

def custom_time_func(row,time1,time2,time3,time4):
    if row['CRASH TIME']>=str(time4) or row['CRASH TIME']<str(time1):
        return "MID NIGHT"
    elif row['CRASH TIME']>=str(time1) and row['CRASH TIME']<str(time2):
        return "MORNING"
    elif row['CRASH TIME']>=str(time2) and row['CRASH TIME']<str(time3):
        return "AFTERNOON"
    elif row['CRASH TIME']>= str(time3) and row['CRASH TIME']<str(time4):
        return "NIGHT"

df['CRASH DAYTIME'] = df.apply(custom_time_func,args=(time1,time2,time3,time4),axis=1)
df['MAJOR ACCIDENT TYPE 1'] = df.apply(custom_acc_type, column=1 , axis=1)
df4 = df.groupby(by='MAJOR ACCIDENT TYPE 1')

def plot_pie_chart(df,title):
    plt.pie(df,labels = df.index,
                    autopct = '%1.1f%%',shadow = True,
                    startangle = 0,
                    wedgeprops = {"edgecolor":"black",
                            'linewidth': 2,
                            'antialiased': True})
    plt.axis('equal')  
    plt.title(title)

val = 1
for name, data_group in df4:
    df3 = data_group.groupby(by='CRASH DAYTIME').count()
    df3 = pd.Series(df3['CRASH DATE'])
    plt.subplot(2,4,val)
    plot_pie_chart(df3,name)
    val+=1

plt.show()