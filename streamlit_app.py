import streamlit as st
import pandas as pd

# Configuração inicial
st.set_page_config(page_title="Exemplo gurias", page_icon=":beer:", layout="wide")

# Título da página
st.title("Gurias")

# subtítulo
st.subheader('Esse é um exemplo')

# Parágrafo
st.write("Este é um exemplo de aplicativo Streamlit.")

# Botão
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")
