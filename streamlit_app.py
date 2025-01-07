import streamlit as st
import pandas as pd
import plotly.express as px


# Configuração inicial
st.set_page_config(page_title="Exemplo gurias", page_icon=":beer:", layout="wide")

# Título da página
st.title("Gurias")

# Leitura dos dados de dengue
dados = pd.read_csv('dengue_resid_csv_2025.csv', encoding = 'latin1')


# Fazer um gráfico de casos por ano
# Agrupar os dados por ano e somar os casos confirmados
casos_por_ano = dados.groupby('Ano')['Confirmados'].sum().reset_index()

# Criar o gráfico de barras
fig = px.bar(casos_por_ano, x='Ano', y='Confirmados', title='Casos Confirmados de Dengue por Ano',
             labels={'Ano': 'Ano', 'Confirmados': 'Casos Confirmados'},
             text='Confirmados')

# Adicionar texto sobre as barras
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Mostrar a figura
st.plotly_chart(fig)

