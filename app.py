import streamlit as st
import pickle
import pandas as pd
import numpy as np


orbit = [i for i in range(0,10)]
pipe = pickle.load(open('saved_model.pkl','rb'))
st.title('Asteroid Classification')
st.image('first.jpg', caption='Asteroid', use_column_width=True)
Absolute_Magnitude = st.number_input('Enter Absolute Magnitude(11-32) :')
col1,col2 = st.columns(2)
with col1:
    Est_Dia_in_KM_min = st.number_input('Enter Est_Dia_in_KM(min) :')
with col2:
    Est_Dia_in_KM_max = st.number_input('Enter Est_Dia_in_KM(max) :')
Epoch_Date_Close_Approach = st.number_input('Enter Epoch Date Close Approach :')
Relative_Velocity_km_per_sec = st.number_input('Enter Relative Velocity km per sec :')
Miles_per_hour = st.number_input('Enter Miles per hour :')
Miss_Dist_kilometers = st.number_input('Enter Miss Dist.(kilometers) :')
Orbit_Uncertainity = st.number_input('Enter the Orbit Uncertainity(1,10):')
Minimum_Orbit_Intersection = st.number_input('Enter the Minimum Orbit Intersection :')

if st.button('Predict Hazardous :'):
    # df = pd.DataFrame(
    #     {
    #         'Absolute Magnitude':[Absolute_Magnitude],
    #         'Est Dia in KM(min)':[Est_Dia_in_KM_min],
    #         'Est Dia in KM(max)':[Est_Dia_in_KM_max],
    #         'Epoch Date Close Approach':[Epoch_Date_Close_Approach],
    #         'Relative Velocity km per sec':[Relative_Velocity_km_per_sec],
    #         'Miles per hour':[Miles_per_hour],
    #         'Miss Dist.(kilometers)':[Miss_Dist_kilometers],
    #         'Orbit Uncertainity':[Orbit_Uncertainity],
    #         'Minimum Orbit Intersection':[Minimum_Orbit_Intersection]
    #     }
    # )
    data = [Absolute_Magnitude,Est_Dia_in_KM_min,Est_Dia_in_KM_min,Epoch_Date_Close_Approach,Relative_Velocity_km_per_sec,Miles_per_hour,Miss_Dist_kilometers,Orbit_Uncertainity,Minimum_Orbit_Intersection]
    df=np.array([data])
    result = int(pipe.predict(df)[0])
    if result:
        st.header('Asteroid is Hazardous...')
    else:
        st.header('Asteroid is Not Hazardous...')
    

