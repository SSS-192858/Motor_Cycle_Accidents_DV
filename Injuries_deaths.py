import pandas as pd
from datetime import time
import matplotlib.pyplot as plt
from cleanupFile import cleanUp
    
def count_func(df1: pd.DataFrame,param,dict):
    for i,row in df1.iterrows():
        dict[row['BOROUGH']][0]+=row['NUMBER OF PEDESTRAINS '+param]
        dict[row['BOROUGH']][1]+=row['NUMBER OF CYCLIST '+param]
        dict[row['BOROUGH']][2]+=row['NUMBER OF MOTORIST '+param]
    
def plot_func(dict, param):
       
    df2=pd.DataFrame.from_dict(dict,orient='index',columns=['PEDESTRIANS '+param,'CYCLIST '+param,'MOTORIST '+param])

    plt.bar(df2.index,df2['PEDESTRIANS '+param],color='r')
    plt.bar(df2.index,df2['CYCLIST '+param],bottom=df2['PEDESTRIANS '+param],color='b')
    plt.bar(df2.index,df2['MOTORIST '+param],bottom=df2['CYCLIST '+param]+df2['PEDESTRIANS '+param],color='g')
    plt.xlabel("Boroughs")
    param1 = "Deaths" if param=="KILLED" else "Injuries"
    plt.ylabel(param1)
    plt.legend(["PEDESTRIANS "+param, "CYCLIST "+param, "MOTORIST "+param])
    plt.title(f"Borough and {param1}")
    plt.show()

if __name__ == "__main__":

    df = pd.read_csv("Dataset1.csv")
    cleanUp(df)
    groups = df.groupby(by=['BOROUGH'])

    dict1 = {}
    for name, group in groups:
        dict1[name] = [0,0,0]

    count_func(df,"KILLED",dict1)
    plot_func(dict1, "KILLED")

    dict2 = {}
    for name, group in groups:
        dict2[name] = [0,0,0]

    count_func(df,"INJURED",dict2)
    plot_func(dict2, "INJURED")