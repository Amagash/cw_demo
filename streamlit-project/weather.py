import streamlit as st
from configparser import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import configparser

# get the directory name and file name of the script
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
print(dirname)
print(filename)
# read the configuration file
config = configparser.ConfigParser()
config.read(os.path.join(dirname, "configuration.ini"))
print(config)

# get the input file name from the configuration file
input_file = config.get("input_data", "input_file")

data_file_name = f"{input_file}"

#function to load data file into a data frame and return the dataframe, decorate it as cache
@st.cache_data
def load_data(data_file_name):
    df = pd.read_csv(data_file_name)
    return df

df = load_data(data_file_name)
# convert DATE field to datetime type
df['DATE'] = pd.to_datetime(df['DATE'])

st.write('''

# :mostly_sunny: Weather Data Visualization :snow_cloud:

---

    ''')

tab_data_set, tab_data_visualization = st.tabs(['Data set', 'Single City Charts']) 

#first tab shows the dataframe 
with tab_data_set:
    st.write(df)


#second tab shows chart from the dataframe 
with tab_data_visualization:
    #get distinct values of the column Country in the dataframe sorted 
    countries = sorted(df['Country'].unique())
    #streamlit selectbox to choose the country 
    country = st.selectbox('Select a country', countries)
    #get distinct values of the column StationName in the dataframe where country is selected 
    stations = sorted(df[df['Country'] == country]['StationName'].unique())
    #streamlit selectbox to choose the station 
    station = st.selectbox('Select a station', stations)
    #get the data frame where country and station is selected 
    country_station = df[(df['Country'] == country) & (df['StationName'] == station)]
    #get maximum and minimum date from the data frame and convert it to datetime type 
    min_date = country_station['DATE'].min().to_pydatetime() 
    max_date = country_station['DATE'].max().to_pydatetime() 
    #streamlit range slider to chose the date between min_date and max_date 
    date_range = st.slider('Select a date', min_value=min_date, max_value=max_date,
                           value=(min_date, max_date))

    df_plot_daterange = country_station[(country_station['DATE']>=date_range[0]) & (country_station['DATE']<=date_range[1])] 
    #plot TMAX(max temperature),TMIN(min temperature) and TAVG(average temperature) over DATE in df_country_station using seaborn 
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='DATE', y='TMAX', data=df_plot_daterange, label='TMAX')
    sns.lineplot(x='DATE', y='TMIN', data=df_plot_daterange, label='TMIN')
    sns.lineplot(x='DATE', y='TAVG', data=df_plot_daterange, label='TAVG')
    ax.set_title(f'Temperatures in {country} for {station}')
    plt.legend()
    st.pyplot(fig)

