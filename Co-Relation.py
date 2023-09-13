import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_up(df):
    df.drop(columns=['CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5'], inplace=True)
    df.dropna(subset=['BOROUGH'], inplace=True)
    df.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    df = df[df['LATITUDE']!=0]
    df = df[df['LONGITUDE']!=0]


def custom_acc_type(row,groupingDictionary):
    for j in groupingDictionary.keys():
       if row['CONTRIBUTING FACTOR VEHICLE 1'] in groupingDictionary[j]:
           return j
       
groupingDictionary = {
    "Distraction" : ["Driver Inattention/Distraction", "Outside Car Distraction", "Passenger Distraction", "Glare", "Cell Phone (hand-held)", "Cell Phone (hands-free)", "Other Electronic Device"], 
    "Car Defects" : ["Accelerator Defective", "Brakes Defective", "Headlights Defective", "Other Lighting Defects", "Steering Failure", "Tire Failure/Inadequate", "Tow Hitch Defective", "Windshield Inadequate"],
    "Substance Abuse" : ["Alcohol Involvement", "Drugs (Illegal)", "Prescription Medication"],
    "Driver not at fault" : ["Animals Action", "Lane Marking Improper/Inadequate", "Obstruction/Debris", "Other Vehicular", "Pavement Defective", "Pavement Slippery", "Pedestrian/Bicyclist/Other Pedestrian Error/Confusion", "Reaction to Other Uninvolved Vehicle", "Shoulders Defective/Improper", "Traffic Control Device Improper/Non-Working", "View Obstructed/Limited"], 
    "Driver Inexperience" : ["Driver Inexperience"], 
    "Medical/Fatigue" : ["Fatigued/Drowsy", "Fell Asleep", "Illness", "Lost Consciousness", "Physical Disability"], 
    "Traffic Rule Violation" : ["Aggressive Driving/Road Rage", "Backing Unsafely", "Failure to Keep Right", "Failure to Yield Right-of-Way", "Following Too Closely", "Oversized Vehicle", "Passing Too Closely", "Passing or Lane Usage Improper", "Traffic Control Disregarded", "Turning Improperly", "Unsafe Lane Changing", "Unsafe Speed"]
}    

df = pd.read_csv('Dataset1.csv')
df1 = df[df['CRASH DATE']>='2013-01-01']
df1 = df1[df1['CRASH DATE']<='2013-12-31']
df1.sort_values(by='CRASH DATE',inplace=True)


df1['MAJOR ACCIDENT TYPE 1'] = df1.apply(custom_acc_type,axis=1)
df2 = df1.groupby(by='MAJOR ACCIDENT TYPE 1')['NUMBER OF PERSONS KILLED'].sum()
df3 = df1.groupby(by='MAJOR ACCIDENT TYPE 1')['NUMBER OF PERSONS INJURED'].sum()

df2.plot.bar()
plt.title("Deaths vs Reason of Accident")
plt.show()

df3.plot.bar()
plt.title("Injuries vs Reason of accidents")
plt.show()
