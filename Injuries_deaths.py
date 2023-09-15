import pandas as pd
from datetime import time
import matplotlib.pyplot as plt

def custom_month_func(row):
    if row['CRASH DATE']>="2013-01-01" and row['CRASH DATE']<="2013-01-31":
        return "JAN-2013"
    elif row['CRASH DATE']>="2013-02-01" and row['CRASH DATE']<="2013-02-28":
        return "FEB-2013"
    elif row['CRASH DATE']>="2012-03-01" and row['CRASH DATE']<="2013-03-31":
        return "MAR-2013"
    elif row['CRASH DATE']>="2013-04-01" and row['CRASH DATE']<="2013-04-30":
        return "APR-2013"
    elif row['CRASH DATE']>="2013-05-01" and row['CRASH DATE']<="2013-05-31":
        return "MAY-2013"
    elif row['CRASH DATE']>="2013-06-01"and row['CRASH DATE']<="2013-06-30":
        return "JUN-2013"
    if row['CRASH DATE']>="2013-07-01" and row['CRASH DATE']<="2013-07-31":
        return "JUL-2013"
    elif row['CRASH DATE']>="2013-08-01" and row['CRASH DATE']<="2013-08-31":
        return "AUG-2013"
    elif row['CRASH DATE']>="2013-09-01" and row['CRASH DATE']<="2013-09-30":
        return "SEPT-2013"
    elif row['CRASH DATE']>="2013-10-01" and row['CRASH DATE']<="2013-10-31":
        return "OCT-2013"
    elif row['CRASH DATE']>="2013-11-01" and row['CRASH DATE']<="2013-11-30":
        return "NOV-2013"
    elif row['CRASH DATE']>="2013-12-01"and row['CRASH DATE']<="2013-12-31":
        return "DEC-2013"
    
def monthwise_count_func(df1,param,dict):
    for i,row in df1.iterrows():
        if row['CRASH_MONTH']=='JAN-2013':
            dict['JAN-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['JAN-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['JAN-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='FEB-2013':
            dict['FEB-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['FEB-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['FEB-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='MAR-2013':
            dict['MAR-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['MAR-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['MAR-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='APR-2013':
            dict['APR-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['APR-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['APR-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='MAY-2013':
            dict['MAY-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['MAY-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['MAY-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='JUN-2013':
            dict['JUN-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['JUN-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['JUN-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='JUL-2013':
            dict['JUL-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['JUL-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['JUL-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='AUG-2013':
            dict['AUG-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['AUG-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['AUG-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='SEPT-2013':
            dict['SEPT-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['SEPT-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['SEPT-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='OCT-2013':
            dict['OCT-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['OCT-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['OCT-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='NOV-2013':
            dict['NOV-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['NOV-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['NOV-2013'][2]+=row['NUMBER OF MOTORIST '+param]
        elif row['CRASH_MONTH']=='DEC-2013':
            dict['DEC-2013'][0]+=row['NUMBER OF PEDESTRIANS '+param]
            dict['DEC-2013'][1]+=row['NUMBER OF CYCLIST '+param]
            dict['DEC-2013'][2]+=row['NUMBER OF MOTORIST '+param]
    
    print(dict)
    df2=pd.DataFrame.from_dict(dict,orient='index',columns=['PEDESTRIANS '+param,'CYCLIST '+param,'MOTORIST '+param])
    df2
    print(df2.index)

    plt.bar(df2.index,df2['PEDESTRIANS '+param],color='r')
    plt.bar(df2.index,df2['CYCLIST '+param],bottom=df2['PEDESTRIANS '+param],color='b')
    plt.bar(df2.index,df2['MOTORIST '+param],bottom=df2['CYCLIST '+param]+df2['PEDESTRIANS '+param],color='g')
    plt.xlabel("Months of 2012")
    if param == "KILLED":
        plt.ylabel("Deaths")
    else:
        plt.ylabel('Injuries')
    plt.legend(["PEDESTRIANS "+param, "CYCLIST "+param, "MOTORIST "+param])
    plt.title("Deaths vs Months ("+name+")")
    # plt.yticks([0,10,20,30,40])
    plt.show()

df = pd.read_csv("Dataset1.csv")
df.drop(columns=['CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5'], inplace=True)

df1 = df[df['CRASH DATE']>='2013-01-01']
df1 = df1[df1['CRASH DATE']<='2013-12-31']
df1.sort_values(by='CRASH DATE',inplace=True)
df1['CRASH_MONTH'] = df1.apply(custom_month_func,axis=1)

dict1 = {
    "JAN-2013":[0,0,0],
    "FEB-2013":[0,0,0],
    "MAR-2013":[0,0,0],
    "APR-2013":[0,0,0],
    "MAY-2013":[0,0,0],
    "JUN-2013":[0,0,0],
    'JUL-2013':[0,0,0],
    'AUG-2013':[0,0,0],
    'SEPT-2013':[0,0,0],
    'OCT-2013':[0,0,0],
    'NOV-2013':[0,0,0],
    'DEC-2013':[0,0,0]
}

monthwise_count_func(df1,"KILLED",dict1)

dict1 = {
    "JAN-2013":[0,0,0],
    "FEB-2013":[0,0,0],
    "MAR-2013":[0,0,0],
    "APR-2013":[0,0,0],
    "MAY-2013":[0,0,0],
    "JUN-2013":[0,0,0],
    'JUL-2013':[0,0,0],
    'AUG-2013':[0,0,0],
    'SEPT-2013':[0,0,0],
    'OCT-2013':[0,0,0],
    'NOV-2013':[0,0,0],
    'DEC-2013':[0,0,0]
}

custom_month_func(df1,"INJURED",dict1)
print(dict1)
df2=pd.DataFrame.from_dict(dict,orient='index',columns=['PEDESTRIANS INJURED','CYCLIST INJURED','MOTORIST INJURED'])
df2

groups = df1.groupby(by=['BOROUGH'])
for name, group1 in groups:
    df2 = df1[df1['BOROUGH'] == name]
    dict = {
        "JAN-2013":[0,0,0],
        "FEB-2013":[0,0,0],
        "MAR-2013":[0,0,0],
        "APR-2013":[0,0,0],
        "MAY-2013":[0,0,0],
        "JUN-2013":[0,0,0],
        'JUL-2013':[0,0,0],
        'AUG-2013':[0,0,0],
        'SEPT-2013':[0,0,0],
        'OCT-2013':[0,0,0],
        'NOV-2013':[0,0,0],
        'DEC-2013':[0,0,0]
    }
    monthwise_count_func(df1,"KILLED",dict)

for name, group1 in groups:
    df2 = df1[df1['BOROUGH'] == name]
    dict = {
        "JAN-2013":[0,0,0],
        "FEB-2013":[0,0,0],
        "MAR-2013":[0,0,0],
        "APR-2013":[0,0,0],
        "MAY-2013":[0,0,0],
        "JUN-2013":[0,0,0],
        'JUL-2013':[0,0,0],
        'AUG-2013':[0,0,0],
        'SEPT-2013':[0,0,0],
        'OCT-2013':[0,0,0],
        'NOV-2013':[0,0,0],
        'DEC-2013':[0,0,0]
    }
    monthwise_count_func(df1,"INJURED",dict)