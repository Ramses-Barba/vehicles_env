import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header("Graficos histo-dispersion")
 
        
if st.checkbox('Construir un histograma'): #             
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches'): 

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



