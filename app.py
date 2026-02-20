# importando bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

# título do app
st.header('Dashboard de Anúncios de Veículos')

# carregar dados
car_data = pd.read_csv('vehicles.csv')  # o CSV precisa estar na mesma pasta do app.py

# botão para histograma
if st.button('Criar histograma de odômetro'):
    st.write('Histograma da coluna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# botão para gráfico de dispersão
if st.button('Criar gráfico de dispersão preço x odômetro'):
    st.write('Dispersão entre odometer e price')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
