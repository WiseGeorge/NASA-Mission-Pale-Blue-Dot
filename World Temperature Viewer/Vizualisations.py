import altair as alt
import pandas as pd
import streamlit as st

import altair as alt
import pandas as pd
import streamlit as st
import numpy as np

from vega_datasets import data


def TC_Pie_Plot(total_countries, total_condition, condition, color_condition):
    # Crear DataFrame
    data = pd.DataFrame({
        'Category': ['Total Countries', condition],
        'Total': [total_countries, total_condition]
    })

    # Calcular porcentajes
    data['Percentage'] = round(data['Total'] / data['Total'].sum() * 100, 1)
    data['Percentage_cumsum'] = data['Percentage'].cumsum() * 2 * np.pi

    # Definir colores
    #colors = ['green' if cat == 'Total Countries' else 'darkblue' if color_condition == 0 else 'darkred' for cat in data['Category']]
    #colors = ['lightgreen' if cat == 'Total Countries' else 'lightcoral' if color_condition == 0 else 'lightskyblue' for cat in data['Category']]
    
    if color_condition == 1:
        colors = ['lightcoral', 'indianred']  # Tonos de rojo
    else:
        colors = ['lightskyblue', 'steelblue']


    # Crear gráfico de pastel
    chart = alt.Chart(data).mark_arc().encode(
        theta=alt.Theta('Percentage:Q', stack=True),
        color=alt.Color('Category:N', scale=alt.Scale(domain=data['Category'].unique(), range=colors)),
        tooltip=['Category', 'Total', 'Percentage']
    ).properties(
        width=400,
        height=400, 
    )

    chart = chart.interactive()
    # Mostrar gráfico en Streamlit
    st.altair_chart(chart,use_container_width=True)



def GlobeT_Chart(usa_data):
    col1, col2, col3 = st.columns([2,2,6])
    with col1: 
        # Lista de proyecciones disponibles
        projections = ['naturalEarth1', 'gnomonic','albers', 'albersUsa', 'azimuthalEqualArea', 'azimuthalEquidistant', 'conicEqualArea', 'conicEquidistant', 'equirectangular', 'mercator', 'orthographic', 'stereographic', 'transverseMercator', 'equalEarth']
        # Crea la selectbox en Streamlit
        selected_projection = st.selectbox('Projection Type:', projections)

    with col2:
        # Crear un diccionario para mapear los nombres de los meses a números
        month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        # Crear un select box para el mes
        month_to_filter = st.selectbox('Month', list(month_dict.keys()))
        # Convertir el mes seleccionado a número
        month_to_filter = month_dict[month_to_filter]

    with col3:
         # Crear un select box para el año
        year_to_filter = st.slider('Year', min_value=int(usa_data['Year'].min()), max_value=int(usa_data['Year'].max()), value=int(usa_data['Year'].min()))

       
    # Filtra los datos para el año y mes seleccionados
    filtered_data = usa_data[(usa_data['Year'] == year_to_filter) & (usa_data['Month'] == month_to_filter)]
    print(filtered_data)
    # Carga un mapa del mundo
    usa = alt.topo_feature(data.world_110m.url, 'countries')

    # Crea el gráfico de fondo con el mapa del mundo
    background = alt.Chart(usa).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project(selected_projection)

    # Crea el gráfico de puntos con los datos de temperatura
    points = alt.Chart(filtered_data).mark_circle().encode(
        longitude='Longitude:Q',
        latitude='Latitude:Q',
        color=alt.Color('AverageTemperature:Q', scale=alt.Scale(domain=[-20, 0, 20, 40], range=['darkblue', 'blue', 'white', 'red'])),
        tooltip=['Country:N','City:N', 'AverageTemperature:Q']
    )

    # Combina los gráficos
    chart = background + points
    chart = chart.interactive()
    # Muestra el gráfico en Streamlit
    st.altair_chart(chart, use_container_width=True)

    # Obtén la fila con la temperatura máxima
    max_temp_data = filtered_data.loc[filtered_data['AverageTemperature'].idxmax()]

    # Obtén la fila con la temperatura mínima
    min_temp_data = filtered_data.loc[filtered_data['AverageTemperature'].idxmin()]

    # Display the data in a text format
    st.write(f'###### 🔥 The :orange[**highest monthly**] temperature for {month_list[month_to_filter-1]}, {year_to_filter} is: :orange[**{round(max_temp_data["AverageTemperature"],1)}**]. Located in :orange[**{max_temp_data["Country"]}: {max_temp_data["City"]}**].')
    
    st.write(f'###### ❄️ The :blue[**lowest monthly**] temperature for {month_list[month_to_filter-1]}, {year_to_filter} is: :blue[**{min_temp_data["AverageTemperature"]}**]. Located in :blue[**{min_temp_data["Country"]}: {min_temp_data["City"]}**].')


def USAT_Chart(usa_data):

    col1, col2 = st.columns([2,6])
  
    with col1:
        # Crear un diccionario para mapear los nombres de los meses a números
        month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        # Crear un select box para el mes
        month_to_filter = st.selectbox('Month', list(month_dict.keys()), key=100)
        # Convertir el mes seleccionado a número
        month_to_filter = month_dict[month_to_filter]

    with col2:
         # Crear un select box para el año
        year_to_filter = st.slider('Year', min_value=int(usa_data['Year'].min()), max_value=int(usa_data['Year'].max()), value=int(usa_data['Year'].min()), key=101)

     # Filtra los datos para el año y mes seleccionados
    filtered_data = usa_data[(usa_data['Year'] == year_to_filter) & (usa_data['Month'] == month_to_filter)]
    
    # Charts
    us_states = alt.topo_feature(data.us_10m.url, 'states')
    # Crea el gráfico de fondo con el mapa del mundo
    usabackground = alt.Chart(us_states).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project('albersUsa')

    usapoints = alt.Chart(filtered_data).mark_circle().encode(
        longitude='Longitude:Q',
        latitude='Latitude:Q',
        color=alt.Color('AverageTemperature:Q', scale=alt.Scale(domain=[-20, 0, 20, 40], range=['darkblue', 'blue', 'white', 'red'])),
        tooltip=['Country:N','City:N', 'AverageTemperature:Q']
    )

    chart = usabackground + usapoints
    chart = chart.interactive()
    # Display
    st.altair_chart(chart, use_container_width=True)

    # Obtén la fila con la temperatura máxima
    max_temp_data = filtered_data.loc[filtered_data['AverageTemperature'].idxmax()]

    # Obtén la fila con la temperatura mínima
    min_temp_data = filtered_data.loc[filtered_data['AverageTemperature'].idxmin()]

    # Display the data in a text format
    
    st.write(f'###### 🔥 The :orange[**highest monthly**] temperature for {month_list[month_to_filter-1]}/{year_to_filter} is: :orange[**{round(max_temp_data["AverageTemperature"],1)}**]. Located in :orange[**{max_temp_data["City"]}**].')
    
    st.write(f'###### ❄️ The :blue[**lowest monthly**] temperature for {month_list[month_to_filter-1]}/{year_to_filter} is: :blue[**{min_temp_data["AverageTemperature"]}**]. Located in :blue[**{min_temp_data["City"]}**].')
