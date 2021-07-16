# streamlit run app.py
# pip install -r requirements.txt

import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

# st.title('Rain Prediction')
# st.markdown("<h1 style='text-align: center; color: black;'>Rain Prediction</h1>", unsafe_allow_html=True)
im = Image.open("cover.png")
st.image(im, width=700)

html_temp = """
<div style="width:700px;background-color:maroon;padding:10px">
<h1 style="color:white;text-align:center;">Rain Prediction ML App. (Demo)</h1>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

# # images
# im = Image.open("image.png")
# st.image(im, width=700)

# @st.cache
# bir buyuk bir datatyi read_csv ile tekrar tekrar okutmamak icin hafuzada tutmasi icin st.cache kullanilir.
model = pickle.load(open("model.pkl","rb"))

# Features: ["Contract", "InternetService", "Dependents", "OnlineSecurity",'TechSupport',"PaymentMethod",'Partner','Tenure','TotalCharges']

locations = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree',
       'Newcastle', 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond',
       'Sydney', 'SydneyAirport', 'WaggaWagga', 'Williamtown',
       'Wollongong', 'Canberra', 'Tuggeranong', 'MountGinini', 'Ballarat',
       'Bendigo', 'Sale', 'MelbourneAirport', 'Melbourne', 'Mildura',
       'Nhil', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
       'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa',
       'Woomera', 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport',
       'Perth', 'SalmonGums', 'Walpole', 'Hobart', 'Launceston',
       'AliceSprings', 'Darwin', 'Katherine', 'Uluru']

WindDir = ['W', 'WNW', 'WSW', 'NE', 'NNW', 'N', 'NNE', 'SW','ENE', 'SSE', 'S', 'NW', 'SE', 'ESE', 'E', 'SSW']

st.sidebar.header("Configure the Weather Features of Today:")
MinTemp = st.sidebar.slider("Minimum Temperature (Celcius)", -10,50,10, step=1)
MaxTemp = st.sidebar.slider("Maximum Temperature (Celcius)", -10,50,20, step=1)
Rainfall = st.sidebar.slider("Rainfall (milimetres)", 0,400,0, step=1)
Evaporation = st.sidebar.slider("Evaporation (milimetres)", 0,150,20, step=1)
Sunshine = st.sidebar.slider("Sunshine (hours)", 0,15,5, step=1)
WindGustSpeed = st.sidebar.slider("Maximum Wind Gust Speed (km per hour)", 0,150,80, step=1)
WindSpeed9am = st.sidebar.slider("Wind Speed at 9am (km per hour)", 0,15,50, step=1)
WindSpeed3pm = st.sidebar.slider("Wind Speed at 3pm (km per hour)", 0,15,25, step=1)
Humidity9am = st.sidebar.slider("Relative Humudity at 9am (percent)", 0,100,50, step=1)
Humidity3pm = st.sidebar.slider("Relative Humudity at 3pm (percent)", 0,100,50, step=1)
Pressure9am = st.sidebar.slider("Atmospheric Pressure at 9am (hectopascals)", 950,1050,1000, step=1)
Pressure3pm = st.sidebar.slider("Atmospheric Pressure at 3pm (hectopascals)", 950,1050,1000, step=1)
Cloud9am = st.sidebar.slider("Fraction of sky obscured by cloud at 9am (eighths)", 0,10,5, step=1)
Cloud3pm = st.sidebar.slider("Fraction of sky obscured by cloud at 3pm (eighths)", 0,10,5, step=1)
Temp9am = st.sidebar.slider("Temperature at 9am (Celcius)", -10,50,10, step=1)
Temp3pm = st.sidebar.slider("Temperature at 3pm (Celcius)", -10,50,10, step=1)
RainToday = 1 if Rainfall>0 else 0
Month = st.sidebar.slider("Number of the Month", 1,12,6, step=1)
DiffTemp = MaxTemp - MinTemp
Location = st.sidebar.selectbox("Location",(locations))
WindGustDir = st.sidebar.selectbox("Direction of Strongest Gust",(WindDir))
WindDir9am = st.sidebar.selectbox("Direction of Wind at 9am",(WindDir))
WindDir3pm = st.sidebar.selectbox("Direction of Wind at 3pm",(WindDir))

my_dict = {'MinTemp': MinTemp,
             'MaxTemp': MaxTemp,
             'Rainfall': Rainfall,
             'Evaporation': Evaporation,
             'Sunshine': Sunshine,
             'WindGustSpeed': WindGustSpeed,
             'WindSpeed9am': WindSpeed9am,
             'WindSpeed3pm': WindSpeed3pm,
             'Humidity9am': Humidity9am,
             'Humidity3pm': Humidity3pm,
             'Pressure9am': Pressure9am,
             'Pressure3pm': Pressure3pm,
             'Cloud9am': Cloud9am,
             'Cloud3pm': Cloud3pm,
             'Temp9am': Temp9am,
             'Temp3pm': Temp3pm,
             'RainToday': RainToday,
             'Month': Month,
             'DiffTemp': DiffTemp,
             'Location':Location,
             'WindGustDir':WindGustDir,
             'WindDir9am':WindDir9am,
             'WindDir3pm':WindDir3pm,
             }

df = pd.DataFrame([my_dict])
all_columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
       'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
       'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
       'Temp9am', 'Temp3pm', 'RainToday', 'Month', 'DiffTemp',
       'Location_Brisbane', 'Location_Cairns', 'Location_Canberra',
       'Location_Cobar', 'Location_CoffsHarbour', 'Location_Darwin',
       'Location_Hobart', 'Location_Melbourne', 'Location_MelbourneAirport',
       'Location_Mildura', 'Location_Moree', 'Location_MountGambier',
       'Location_NorfolkIsland', 'Location_Nuriootpa', 'Location_Perth',
       'Location_PerthAirport', 'Location_Portland', 'Location_Sale',
       'Location_Sydney', 'Location_SydneyAirport', 'Location_Townsville',
       'Location_WaggaWagga', 'Location_Watsonia', 'Location_Williamtown',
       'Location_Woomera', 'WindGustDir_ENE', 'WindGustDir_ESE',
       'WindGustDir_N', 'WindGustDir_NE', 'WindGustDir_NNE', 'WindGustDir_NNW',
       'WindGustDir_NW', 'WindGustDir_S', 'WindGustDir_SE', 'WindGustDir_SSE',
       'WindGustDir_SSW', 'WindGustDir_SW', 'WindGustDir_W', 'WindGustDir_WNW',
       'WindGustDir_WSW', 'WindDir9am_ENE', 'WindDir9am_ESE', 'WindDir9am_N',
       'WindDir9am_NE', 'WindDir9am_NNE', 'WindDir9am_NNW', 'WindDir9am_NW',
       'WindDir9am_S', 'WindDir9am_SE', 'WindDir9am_SSE', 'WindDir9am_SSW',
       'WindDir9am_SW', 'WindDir9am_W', 'WindDir9am_WNW', 'WindDir9am_WSW',
       'WindDir3pm_ENE', 'WindDir3pm_ESE', 'WindDir3pm_N', 'WindDir3pm_NE',
       'WindDir3pm_NNE', 'WindDir3pm_NNW', 'WindDir3pm_NW', 'WindDir3pm_S',
       'WindDir3pm_SE', 'WindDir3pm_SSE', 'WindDir3pm_SSW', 'WindDir3pm_SW',
       'WindDir3pm_W', 'WindDir3pm_WNW', 'WindDir3pm_WSW']
df = pd.get_dummies(df).reindex(columns=all_columns, fill_value=0)

# Table
def single_customer():
    my_dict = {'MinTemp': MinTemp,
             'MaxTemp': MaxTemp,
             'Rainfall': Rainfall,
             'Evaporation': Evaporation,
             'Sunshine': Sunshine,
             'WindGustSpeed': WindGustSpeed,
             'WindSpeed9am': WindSpeed9am,
             'WindSpeed3pm': WindSpeed3pm,
             'Humidity9am': Humidity9am,
             'Humidity3pm': Humidity3pm,
             'Pressure9am': Pressure9am,
             'Pressure3pm': Pressure3pm,
             'Cloud9am': Cloud9am,
             'Cloud3pm': Cloud3pm,
             'Temp9am': Temp9am,
             'Temp3pm': Temp3pm,
             'RainToday': RainToday,
             'Month': Month,
             'DiffTemp': DiffTemp,
             'Location':Location,
             'WindGustDir':WindGustDir,
             'WindDir9am':WindDir9am,
             'WindDir3pm':WindDir3pm,
             }
    df_table = pd.DataFrame([my_dict])
#     st.table(df_table) 
    st.write('')
    st.dataframe(data=df_table, width=700, height=400)
    st.write('')

single_customer()


# Button
if st.button("Submit"):
    import time
    with st.spinner("ML Model is loading..."):
        my_bar=st.progress(0)
        for p in range(0,101,10):
            my_bar.progress(p)
            time.sleep(0.1)

            rain_probability= model.predict_proba(df)
            is_rain= model.predict(df)
    
        st.success(f'The Probability of the Rain Tomorrow is %{round(rain_probability[0][1]*100,1)}')
        
        if is_rain[0]:
            st.warning("Rain Tomorrow is YES")
        else:
            st.success("Rain Tomorrow is NO")