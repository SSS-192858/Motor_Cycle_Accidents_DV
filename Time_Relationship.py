import pandas as pd
import matplotlib.pyplot as plt
from datetime import time
from cleanupFile import cleanUp

def custom_time_func(row,time1,time2,time3,time4):
    if row['CRASH TIME']>=str(time4) or row['CRASH TIME']<str(time1):
        return "MID NIGHT"
    elif row['CRASH TIME']>=str(time1) and row['CRASH TIME']<str(time2):
        return "MORNING"
    elif row['CRASH TIME']>=str(time2) and row['CRASH TIME']<str(time3):
        return "AFTERNOON"
    elif row['CRASH TIME']>= str(time3) and row['CRASH TIME']<str(time4):
        return "NIGHT"

def plot_pie_chart(df,title):
    plt.pie(df,labels = df.index,
                    autopct = '%1.1f%%',shadow = True,
                    startangle = 0,
                    wedgeprops = {"edgecolor":"black",
                            'linewidth': 2,
                            'antialiased': True})
    plt.axis('equal')  
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    
    time1 = time(6,00,00)
    time2 = time(12,00,00)
    time3 = time(16,30,00)
    time4 = time(22,00,00)

    df = pd.read_csv("Dataset5.csv")
    cleanUp(df)
    df1 = df
    df1['CRASH_DAYTIME'] = df1.apply(custom_time_func,args=(time1,time2,time3,time4),axis=1)
    df2 = df1.groupby('CRASH_DAYTIME')
    df3 = df2.size()
    plot_pie_chart(df3,"Total Accidents in New York City")

    df5 = df1.groupby(by='CRASH_DAYTIME')['NUMBER OF PERSONS KILLED'].sum()
    df5 = pd.Series(df5)
    plot_pie_chart(df5,"Total deaths in accidents in New York City ")

    df5 = df1.groupby(by='CRASH_DAYTIME')['NUMBER OF PERSONS INJURED'].sum()
    df5 = pd.Series(df5)
    plot_pie_chart(df5,"Total injuries in accidents in New York City")

    groups = df.groupby(by=['BOROUGH'])

    for name, group in groups:
        print(name)
        group['CRASH_DAYTIME'] = group.apply(custom_time_func,args=(time1,time2,time3,time4),axis=1)
        df3 = group.groupby('CRASH_DAYTIME')
        df4 = df3.size()
        plot_pie_chart(df4,"Total accidents in "+name)

        df5 = group.groupby(by='CRASH_DAYTIME')['NUMBER OF PERSONS KILLED'].sum()
        df5 = pd.Series(df5)
        plot_pie_chart(df5,"Total Fatalities in accidents in "+name)

        df5 = group.groupby(by='CRASH_DAYTIME')['NUMBER OF PERSONS INJURED'].sum()
        df5 = pd.Series(df5)
        plot_pie_chart(df5,"Total Injuries in accidents in "+name)