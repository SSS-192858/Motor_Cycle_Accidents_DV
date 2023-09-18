import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleanupFile import cleanUp, custom_acc_type, groupingDictionary_common

if __name__ == "__main__":
       
    groupingDictionary = groupingDictionary_common   

    df = pd.read_csv('Dataset1.csv')
    cleanUp(df)

    df1 = df[df['CRASH DATE']>='2013-01-01']
    df1 = df1[df1['CRASH DATE']<='2013-12-31']
    df1.sort_values(by='CRASH DATE',inplace=True)

    df1['MAJOR ACCIDENT TYPE 1'] = df1.apply(custom_acc_type, column=1 ,axis=1)
    df2 = df1.groupby(by='MAJOR ACCIDENT TYPE 1')['NUMBER OF PERSONS KILLED'].sum()
    df3 = df1.groupby(by='MAJOR ACCIDENT TYPE 1')['NUMBER OF PERSONS INJURED'].sum()

    df2.plot.bar()
    plt.title("Deaths vs Reason of Accident")
    plt.show()

    df3.plot.bar()
    plt.title("Injuries vs Reason of accidents")
    plt.show()
