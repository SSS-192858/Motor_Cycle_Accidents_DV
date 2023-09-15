import pandas as pd
import plotly.express as px
from cleanupFile import cleanUp, custom_acc_type, groupingDictionary_common

if __name__ == "__main__":

    df = pd.read_csv("Dataset5.csv")
    cleanUp(df)
    fig = px.scatter_mapbox(df, lat='LATITUDE', lon='LONGITUDE', color='BOROUGH', zoom=12, height=1200, width=1500)
    fig.update_layout(mapbox_style = "open-street-map")
    fig.show()

    groupingDictionary = groupingDictionary_common
        
    df1 = df[df['CONTRIBUTING FACTOR VEHICLE 1'] != "Unspecified"]

    df1['MAJOR ACCIDENT TYPE 1'] = df1.apply(custom_acc_type,args=1,axis=1)
    
    for name, group in df1:
        df_temp = df1[df1['BOROUGH'] == name]
        df_temp = df_temp.sort_values(by=['MAJOR ACCIDENT TYPE 1'])
        print(name)
        fig = px.scatter_mapbox(df_temp, lat='LATITUDE', lon='LONGITUDE', color='MAJOR ACCIDENT TYPE 1', zoom=12, height=1200, width=1500)
        fig.update_layout(mapbox_style = "open-street-map")
        fig.show()


    df1 = df[df['CONTRIBUTING FACTOR VEHICLE 2'] != "Unspecified"]

    df1['MAJOR ACCIDENT TYPE 2'] = df1.apply(custom_acc_type, args=2,axis=1)

    for name, group in df1:
        df_temp = df1[df1['BOROUGH'] == name]
        df_temp = df_temp.sort_values(by=['MAJOR ACCIDENT TYPE 2'])
        print(name)
        fig = px.scatter_mapbox(df_temp, lat='LATITUDE', lon='LONGITUDE', color='MAJOR ACCIDENT TYPE 2', zoom=12, height=1200, width=1500)
        fig.update_layout(mapbox_style = "open-street-map")
        fig.show()