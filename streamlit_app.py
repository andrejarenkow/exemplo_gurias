import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

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

# Fazer com o seaborn
# Configurar estilo do Seaborn
sns.set(style="whitegrid")

# Criar o gráfico de barras
plt.figure(figsize=(8, 6))
ax = sns.barplot(data=casos_por_ano, x='Ano', y='Confirmados', palette='viridis')

# Adicionar rótulos sobre as barras
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5),
                textcoords='offset points')

# Configurar título e rótulos
plt.title('Casos Confirmados de Dengue por Ano', fontsize=16)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Casos Confirmados', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

st.pyplot(ax)
