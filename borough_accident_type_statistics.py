import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cleanupFile import groupingDictionary_common, cleanUp


def make_series(df: pd.DataFrame):

    groupingDictionary = groupingDictionary_common

    df1 = df[df['CONTRIBUTING FACTOR VEHICLE 1'] != "Unspecified"]
    df1 = df1.sort_values(by=['CONTRIBUTING FACTOR VEHICLE 1'])
    df_temp1 = df1.groupby(by=['CONTRIBUTING FACTOR VEHICLE 1'])
    s3 = df_temp1.size()

    df2 = df[df['CONTRIBUTING FACTOR VEHICLE 2'] != "Unspecified"]
    df2 = df2.sort_values(by=['CONTRIBUTING FACTOR VEHICLE 2'])
    df_temp2 = df2.groupby(by=['CONTRIBUTING FACTOR VEHICLE 2'])
    s4 = df_temp2.size()

    df_equal = df[df['CONTRIBUTING FACTOR VEHICLE 1'] == df['CONTRIBUTING FACTOR VEHICLE 2']]
    df_equal = df_equal[df_equal['CONTRIBUTING FACTOR VEHICLE 1'] != "Unspecified"]
    df_equal = df_equal.sort_values(by=['CONTRIBUTING FACTOR VEHICLE 1'])
    df_equal_temp = df_equal.groupby(by=['CONTRIBUTING FACTOR VEHICLE 1'])
    s5 = df_equal_temp.size()
    s_total_ = s3.add(s4, fill_value=0)
    s_total = s_total_.sub(s5, fill_value=0)

    dc = {}
    for i in groupingDictionary.keys():
        dc[i] = 0

    for i in groupingDictionary.keys():
        for j in groupingDictionary[i]:
            if (j in s_total.index):
                dc[i] += s_total[j]

    return pd.Series(dc)



def plot_series(s_total: pd.Series, name="New York City"):

    bars = s_total.index
    x_pos = range(len(s_total))
    plt.bar(x_pos, s_total.values, width=0.8)
    plt.xlabel("Cause of accident", fontsize=10)
    plt.ylabel("Accidents", fontsize=10)
    plt.title(f"Accidents by type in {name}", fontsize=10)
    plt.xticks(x_pos, bars, fontsize=10, rotation=80)
    plt.yticks(fontsize=10)
    for i in range(len(s_total)):
        plt.text(i, s_total.astype('int32')[i], s_total.astype('int32')[i], ha='center', bbox = dict(facecolor = 'white', alpha =.8), fontsize=10)


df = pd.read_csv("Dataset5.csv")
cleanUp(df)

s = make_series(df)
plot_series(s)
plt.show()

r=-6.0
groups = df.groupby(by=['BOROUGH'])
for name, group in groups:
    s = make_series(group)
    print(name)
    bars = s.index
    x_pos = np.arange(len(s))
    x_pos*=20
    plt.bar(x_pos+r, s.values, width=3, label=name)
    plt.xlabel("Cause of accident", fontsize=10)
    plt.ylabel("Accidents", fontsize=10)
    plt.xticks(x_pos, bars, fontsize=10, rotation=80)
    plt.yticks(fontsize=10)
    r+=3
plt.title("Accidents by type in different boroughs", fontsize=10)
plt.legend()
plt.show()        