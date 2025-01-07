import streamlit as st
import pandas as pd

# Configuração inicial
st.set_page_config(page_title="Exemplo gurias", page_icon=":beer:", layout="wide")

# Título da página
st.title("Gurias")

# Leitura dos dados de dengue
dados = pd.read_csv('dengue_resid_csv_2025.csv', encoding = 'latin1')

# Seleção de ano
ano = st.selectbox(label = 'Selecione o ano', options = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Filtro para ano
filtro_ano = dados['Ano']==ano

# Aplicar filtro
dados_ano = dados[filtro_ano]

# mostrar dados
dados_ano
