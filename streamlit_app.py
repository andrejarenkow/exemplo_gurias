import streamlit as st

# Configuração inicial
st.set_page_config(page_title="Meu App", page_icon=":smile:", layout="wide")

# Título da página
st.title("Meu App")

# Parágrafo
st.write("Este é um exemplo de aplicativo Streamlit.")

# Botão
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")
