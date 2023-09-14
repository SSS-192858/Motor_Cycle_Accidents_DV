import pandas as pd
import plotly.express as px


def clean_up(df):
    df.drop(columns=['CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5'], inplace=True)
    df.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    df.dropna(subset=['BOROUGH'], inplace=True)
    df = df[df['LATITUDE']!=0]
    df = df[df['LONGITUDE']!=0]



df = pd.read_csv("Dataset5.csv")
fig = px.scatter_mapbox(df, lat='LATITUDE', lon='LONGITUDE', color='BOROUGH', zoom=12, height=1200, width=1500)
fig.update_layout(mapbox_style = "open-street-map")
fig.show()

df2 = df.groupby('BOROUGH')
print("+-----------------------+")
print(df2.size())
print("+-----------------------+")


groupingDictionary = {
    "Distraction" : ["Driver Inattention/Distraction", "Outside Car Distraction", "Passenger Distraction", "Glare", "Cell Phone (hand-held)", "Cell Phone (hands-free)", "Other Electronic Device"], 
    "Car Defects" : ["Accelerator Defective", "Brakes Defective", "Headlights Defective", "Other Lighting Defects", "Steering Failure", "Tire Failure/Inadequate", "Tow Hitch Defective", "Windshield Inadequate"],
    "Substance Abuse" : ["Alcohol Involvement", "Drugs (Illegal)", "Prescription Medication"],
    "Driver not at fault" : ["Animals Action", "Lane Marking Improper/Inadequate", "Obstruction/Debris", "Other Vehicular", "Pavement Defective", "Pavement Slippery", "Pedestrian/Bicyclist/Other Pedestrian Error/Confusion", "Reaction to Other Uninvolved Vehicle", "Shoulders Defective/Improper", "Traffic Control Device Improper/Non-Working", "View Obstructed/Limited"], 
    "Driver Inexperience" : ["Driver Inexperience"], 
    "Medical/Fatigue" : ["Fatigued/Drowsy", "Fell Asleep", "Illness", "Lost Consciousness", "Physical Disability"], 
    "Traffic Rule Violation" : ["Aggressive Driving/Road Rage", "Backing Unsafely", "Failure to Keep Right", "Failure to Yield Right-of-Way", "Following Too Closely", "Oversized Vehicle", "Passing Too Closely", "Passing or Lane Usage Improper", "Traffic Control Disregarded", "Turning Improperly", "Unsafe Lane Changing", "Unsafe Speed"]
}


def custom_acc_type(row):
    for j in groupingDictionary.keys():
       if row['CONTRIBUTING FACTOR VEHICLE 1'] in groupingDictionary[j]:
           return j
       
df1 = df[df['CONTRIBUTING FACTOR VEHICLE 1'] != "Unspecified"]

df1['MAJOR ACCIDENT TYPE 1'] = df1.apply(custom_acc_type,axis=1)
 
for name, group in df2:
    df_temp = df1[df1['BOROUGH'] == name]
    df_temp = df_temp.sort_values(by=['MAJOR ACCIDENT TYPE 1'])
    print(name)
    fig = px.scatter_mapbox(df_temp, lat='LATITUDE', lon='LONGITUDE', color='MAJOR ACCIDENT TYPE 1', zoom=12, height=1200, width=1500)
    fig.update_layout(mapbox_style = "open-street-map")
    fig.show()


df1 = df[df['CONTRIBUTING FACTOR VEHICLE 2'] != "Unspecified"]

df1['MAJOR ACCIDENT TYPE 2'] = df1.apply(custom_acc_type,axis=1)

for name, group in df2:
    df_temp = df1[df1['BOROUGH'] == name]
    df_temp = df_temp.sort_values(by=['MAJOR ACCIDENT TYPE 2'])
    print(name)
    fig = px.scatter_mapbox(df_temp, lat='LATITUDE', lon='LONGITUDE', color='MAJOR ACCIDENT TYPE 2', zoom=12, height=1200, width=1500)
    fig.update_layout(mapbox_style = "open-street-map")
    fig.show()