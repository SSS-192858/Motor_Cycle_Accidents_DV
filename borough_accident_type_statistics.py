import pandas as pd
import matplotlib.pyplot as plt
from cleanupFile import cleanUp, groupingDictionary_common
plt.rcParams['figure.figsize'] = (30,15)

def make_series(df: pd.DataFrame,groupingDictionary:dict):

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
    plt.bar(x_pos, s_total.values, width=0.4)
    plt.xlabel("Cause of accident", fontsize=15)
    plt.ylabel("Accidents", fontsize=15)
    plt.title(f"Accidents by type in {name}", fontsize=15)
    plt.xticks(x_pos, bars, fontsize=15)
    plt.yticks(fontsize=15)
    for i in range(len(s_total)):
        plt.text(i, s_total.astype('int32')[i], s_total.astype('int32')[i], ha='center', bbox = dict(facecolor = 'white', alpha =.8), fontsize=15)
    plt.show()


if __name__ == "__main__":

    df = pd.read_csv("Dataset5.csv")
    cleanUp(df)

    groupingDictionary = groupingDictionary_common

    s = make_series(df, groupingDictionary)
    plot_series(s)

    groups = df.groupby(by=['BOROUGH'])
    for name, group in groups:
        s = make_series(group, groupingDictionary)
        print(name)
        plot_series(s, name)