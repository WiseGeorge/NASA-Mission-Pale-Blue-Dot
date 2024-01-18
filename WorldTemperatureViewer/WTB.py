# Common Imports
import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
import plotly.express as px
import plotly.graph_objs as go
import plotly.subplots as sp
import toml

# Preprocesing Imports
import pandas as pd
import time
from PIL import Image

import altair as alt
from vega_datasets import data

# Warning
import warnings
warnings.filterwarnings('ignore')

# Models
from Models_Management import WTV_Models
WTVM = WTV_Models()
model = WTVM.model
cities = WTVM.cities

from Vizualisations import TC_Pie_Plot, GlobeT_Chart, USAT_Chart
#Streamlit Config Functions
image1 = Image.open("WorldTemperatureViewer/Images/globe.jpg")


def predict_future(model, df, periods):
    future = df[['ds']]  # Solo usa las fechas en tu dataframe filtrado
    future = future.append(future.tail(1).assign(ds=lambda x: x.ds + pd.DateOffset(days=1)).tail(periods), ignore_index=True)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]


######################
# Page Title & Config
######################
st.set_page_config(page_title='WTV', layout='wide')
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Función para calcular las estadísticas
def calculate_stats(df, level):
    highest_temp_record = df.loc[df['AverageTemperature'].idxmax()]
    lowest_temp_record = df.loc[df['AverageTemperature'].idxmin()]
    stats = {
        "highest_temp": {
            "country": highest_temp_record['Country'],
            "city": highest_temp_record['City'],
            "temperature": highest_temp_record['AverageTemperature'],
            "date": highest_temp_record['dt']
        },
        "lowest_temp": {
            "country": highest_temp_record['Country'],
            "city": highest_temp_record['City'],
            "temperature": lowest_temp_record['AverageTemperature'],
            "date": lowest_temp_record['dt']
        },
        "highest_avg_annual_temp": df.groupby([level, df['dt'].dt.year])['AverageTemperature'].mean().idxmax(),
        "lowest_avg_annual_temp": df.groupby([level, df['dt'].dt.year])['AverageTemperature'].mean().idxmin(),
        "countries_below_0_degrees_count": len(df[df['AverageTemperature'] < 0][level].unique()),
        "countries_above_35_degrees_count": len(df[df['AverageTemperature'] > 35][level].unique())
    }
    return stats

def get_stats(df):
    # Convertir la columna 'dt' a formato de fecha
    #df['dt'] = pd.to_datetime(df['dt'])

    # Calcular las estadísticas para cada período de tiempo
    general_stats = calculate_stats(df, 'Country')
    stats_1970_2000 = calculate_stats(df[df['dt'].dt.year.between(1970, 2000)], 'Country')
    stats_2000_2013 = calculate_stats(df[df['dt'].dt.year.between(2000, 2013)], 'Country')

    # Calcular el promedio de la diferencia de temperatura
    average_temp_diff = df.groupby(df['dt'].dt.year)['AverageTemperature'].mean().diff().mean()

    # Organizar todos los datos en un diccionario
    world_data_stats = {
        "general": general_stats,
        "1970_2000": stats_1970_2000,
        "2000_2013": stats_2000_2013,
        "average_temp_diff": average_temp_diff
    }

    return world_data_stats

def Author_Component():
    st.sidebar.markdown('---')
    st.sidebar.markdown('### Developed By:')
    st.sidebar.markdown('#### **Jorge Felix Martinez Pazos**')
    st.sidebar.markdown('#### Contact Details:')
    st.sidebar.markdown('##### 📧 **[Email](link.com)** ')
    st.sidebar.markdown('##### 💻 **[GitHub](https://github.com)**: ')
    st.sidebar.markdown('##### 💼 **[LinkedIn](LK.com)**: ')
    st.sidebar.markdown('##### 🎓 **[ResearchGate](asd.com)**: ')
    st.sidebar.markdown('##### Ⓜ️ **[Medium](www.asd.com)**: ')

    

@st.cache_data()
def load_data():
    
    # World Data
    world_data = pd.read_csv('WorldTemperatureViewer/Data/WorldData.csv')
    world_data['dt'] = pd.to_datetime(world_data['dt'])
    world_data['Year'] = world_data['dt'].dt.year

    # USA Data
    usa_filter = world_data['Country']=='United States'
    usa_data = world_data[usa_filter]

    # World Stats
    world_data_stats = get_stats(world_data)
    return world_data, usa_data, world_data_stats



with st.sidebar:
    selected = option_menu(
        menu_title = "",
        options = ["Home","Data", "Model Performance", "Forecasting"],
        icons = ["file-earmark-bar-graph-fill","window-dock", "activity"],
        menu_icon = "image-alt",
        default_index = 0,
        orientation = "vertical",
    )

    # Carga los datos la primera vez que se ejecuta la aplicación
    with st.sidebar:
        loading_message = st.empty()
        loading_message.info('Loading Data...')
        world_data, usa_data, world_data_stats = load_data()
        loading_message.empty()


    if st.button('Refresh', type='secondary'):
        st.cache_data.clear()

    with st.sidebar:
        Author_Component()

col1,col2,col3 = st.columns([1,8,1])
with col2:
    st.title("**🪐NASA's Mission: Pale :blue[Blue Dot] 🌎**")

st.image(image1, use_column_width=True)
st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.write('Our Solution for the NASA mision is focus on the Climate Change Suitable Development Goal. For this we build a set of forecasting models using Prohpet from Meta AI using an Earth Temperature Dataset From 1900 to 2013. The proposed models, the used data and methodology is deteiled in this software which authors call **World Temperature Visor**.')



if selected == "Home":
    st.header('World Temperature Visor (WTV)')

    st.write("""**WTV** is an aplication developed as part of the Nasa Mision: Pale Blue Dot, 
             in order to increase visibility and responsability about climate change and global warming. 
             By providing users with an interactive way of contact with the temperature beheaivor 
             around the globe WTV permit an increase in the knowleadge and reality of this problem, 
             a problem that we create, and we must solve, Together.
            Global Warming and Climate Change **DID EXIST**. Pretend like they not will not make them disapear.""") 

    st.write('#### Why is WTV Usefull? :') 
             
    st.write('###### 📈 Allows to See Posible Potential Temperature Behaivor Around The Globe')
    st.write('###### 📉 Allows to See The Prior Beheivor of Temperature from The Studied Data')
    st.write('###### 📊 Allows a Comparition Between Past and Future Temeratures Around The Globe')
    st.write('###### 🛠️ Allows Access to Insigthfull Content of How the Forecasting Models Were Builded')
    
    st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    
    
    with st.expander('Problem Statement'):
        st.title('Problem Statement:')
        def read_markdown_file(markdown_file):
            return Path(markdown_file).read_text()

        intro_markdown = read_markdown_file("README.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)

if selected=='Data':

    st.title('WTV Data')
    st.write('The Data used during this study was Global Land Temperature By City: which has data from 1900 to 2013. However we will display only data from 1970 to 2013 in order to optimize our aplication since the amount of data is very high and Computationaly Spensive')
    st.write('---')

    with st.expander('Earth Temperature Statistics', True):
        st.subheader("Earth Temperature Statistics")
        st.write('📊 Mainly Statistics, Visualization and Comparision of Earth Temperature Data')
        st.header(' ')
        total_countries = len(world_data['Country'].unique())
        c_above = world_data_stats['general']['countries_above_35_degrees_count']
        c_below = world_data_stats['general']['countries_below_0_degrees_count']
    #thc = world_data_stats['general']['']

        col1,col2 = st.columns([3,3])

        with col1:
            st.write('###### Highest Monthly AVG\n ###### Registered Temperature')
            st.metric(f"{world_data_stats['general']['highest_temp']['country']}: {world_data_stats['general']['highest_temp']['city']}",round(world_data_stats['general']['highest_temp']['temperature'],2),str(world_data_stats['general']['highest_temp']['date']))
            st.write('---')
            st.write('Total of Countries with Monthly Average Temperature Above :red[**40**] Degrees Celsius')
            TC_Pie_Plot(total_countries, c_above, 'Above 40C',1)
            
        with col2:
            st.write('###### Lowest Monthly AVG\n ###### Registered Temperature')
            st.metric(f"{world_data_stats['general']['lowest_temp']['country']}: {world_data_stats['general']['lowest_temp']['city']}",round(world_data_stats['general']['lowest_temp']['temperature'],2), str(world_data_stats['general']['lowest_temp']['date']))
            st.write('---')
            st.write('Total of Countries with Monthly Average Temperature Below :blue[**-10**] Degrees Celsius')
            TC_Pie_Plot(total_countries, c_below, 'Below -10C',0)
    st.write('---')
    st.header(' ')
    
    with st.expander('Earth Geographic Chart',True):
        st.subheader('Earth 🗺️ Geographic Chart')
        st.write('Between :green[**1970 - 2000**], and :green[**2000 - 2013**], there is a monthly increase in global average temperature of :orange[**0.03**] degrees Celsius. The accompanying graphs show a steady increase in temperature as we approach 2013.')

        GlobeT_Chart(world_data)
    

    st.header('')
    with st.expander('United States Geographic Chart',True):
        st.subheader("United States 🗽Geographic Chart")
        st.write('Statistics and Visualization of United States Temperature Data')
        USAT_Chart(usa_data)
    

if selected=='Model Performance':

    st.header('Models Performance & Comparison Between Real and Predicted Values')
    st.subheader(' ')
    col1,col2,col3 = st.columns([3,3,3])
    st.subheader('General Models Metrics')
    st.write('- ###### *AVG-MAE:* Average Mean Absolute Error Across all Forecsting Models')
    st.write('- ###### *AVG-MSE:* Average Mean Squared Error Across all Forecasting Models')
    
    col1,col2 = st.columns([5,5])
    col1.metric('AVG-MAE', 1.53, 'High Performance')
    col2.metric('AVG-MSE', 7.31, 'High Performance')
    
    st.header(" ")
    st.write('---')
    with st.expander('Comparision',True):  
        st.subheader("Select Cities and Dates")
        col1,col2,col3 = st.columns([2,5,2])
        with col2:
            selected_cities = st.multiselect("Cities", cities)
         
        
        def plot_real_vs_forecast(models, city, usacitydf):
            usacitydf = usacitydf.rename(columns={'dt': 'ds'})

            # Asegúrate de que las fechas estén en el formato correcto
            start_date = pd.to_datetime('2010-01-01')
            end_date = pd.to_datetime('2013-12-31')

            # Obtén el modelo para la ciudad especificada
            model = models[city]

            # Filtra el dataframe para la ciudad seleccionada y el rango de fechas
            city_filter = (usacitydf['City'] == city) & (usacitydf['ds'] >= start_date) & (usacitydf['ds'] <= end_date)
            df_city = usacitydf[city_filter]

            # Crea un dataframe con todas las fechas desde start_date hasta end_date
            future_dates = pd.date_range(start=start_date, end=end_date)
            future = pd.DataFrame(future_dates, columns=['ds'])
            
            # Haz la predicción
            forecast = predict_future(model, df_city, 30)
            
            # Crea el gráfico con Altair
            real = alt.Chart(df_city).mark_line().encode(
                x='ds:T', 
                y='AverageTemperature:Q', 
                color=alt.value('blue'),
                tooltip=['ds:T', 'AverageTemperature:Q']
            ).properties(title='Real Values')

            real = real.interactive()
            pred = alt.Chart(forecast).mark_line().encode(
                x='ds:T', 
                y='yhat:Q', 
                color=alt.value('green'),
                tooltip=['ds:T', 'yhat:Q']
            )    

            pred = pred.interactive()
            confidence_interval = pred.mark_area(opacity=0.3).encode(
                y='yhat_upper:Q',
                y2='yhat_lower:Q'
            )
            print(df_city)

            chart = real + pred
            chart = chart.properties(title=f'{city} Temperature Comparison {start_date.year}-{end_date.year}')
            #chart = chart.interactive()
            return chart

        for city in selected_cities:
            chart = plot_real_vs_forecast(model, city, usa_data)
            st.altair_chart(chart,use_container_width=True)


if selected=='Forecasting':

    st.header('Temperature Forecasting of United Stated Cities')
    
    with st.expander('Forecasting of USA Cities', True):
        st.subheader("Select Cities and Dates")
        col1, col2, col3 = st.columns([3,3,3])

        with col1:
            selected_cities = st.multiselect("Cities", cities)
        with col2:
            start_year = st.number_input("Start Year", min_value=2013, max_value=2090, value=2024)
        with col3:
            end_year = st.number_input("End Year", min_value=start_year, max_value=2091, value=2026)

        def plot_forecast_altair_yearly(models, city, start_year, end_year):
            # Asegúrate de que las fechas estén en el formato correcto
            start_date = pd.to_datetime(f'{start_year}-01-01')
            end_date = pd.to_datetime(f'{end_year}-12-31')

            # Obtén el modelo para la ciudad especificada
            model = models[city]

            
            # Crea un dataframe con todas las fechas desde start_date hasta end_date
            future_dates = pd.date_range(start=start_date, end=end_date)
            future = pd.DataFrame(future_dates, columns=['ds'])

            # Haz la predicción
            forecast = model.predict(future)
            
            # Crea el gráfico con Altair
            base = alt.Chart(forecast).encode(x='ds:T')

            forecast_line = base.mark_line(color='green').encode(y='yhat:Q')
            confidence_interval = base.mark_area(opacity=0.3).encode(
                y='yhat_upper:Q',
                y2='yhat_lower:Q'
            )

            chart = forecast_line + confidence_interval
            chart = chart.properties(title=f'{city} Temperature Forecasting')
            chart = chart.interactive()

            return chart


        for city in selected_cities:
            chart = plot_forecast_altair_yearly(model, city, start_year, end_year)
            st.altair_chart(chart, use_container_width=True)
            st.write('---')


