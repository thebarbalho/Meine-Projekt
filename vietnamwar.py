import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("Guerra do Vietnã - Análise de Dados dos Estados Unidos durante a Guerra do Vietnã (1955-1975)")

# Carregar arquivo Excel
import os

arquivo = os.path.join(os.path.dirname(__file__), "vietnamwar.xlsx.xlsx")

# Seleção de aba
aba = st.selectbox(
    "Escolha o conjunto de dados:",
    ["Baixas nas Forças Armadas", "Total de Convocados", "Total Gasto pelo Governo"]
)

# Ler dados
df = pd.read_excel(arquivo, sheet_name=aba)

# Mostrar tabela
st.subheader("Dados")
st.write(df)

# Escolha do tipo de gráfico
tipo_grafico = st.radio(
    "Escolha o tipo de gráfico:",
    ["Linha", "Barra"]
)

# Criar gráfico
st.subheader("Visualização")

fig, ax = plt.subplots()

x = df.iloc[:, 0]
y = df.iloc[:, 1]

if tipo_grafico == "Linha":
    ax.plot(x, y, marker='o')
else:
    ax.bar(x, y)

ax.set_xlabel("Ano")
ax.set_ylabel("Valor")

# Título dinâmico
if aba == "Baixas":
    ax.set_title("Mortes de soldados dos EUA")
elif aba == "Convocados":
    ax.set_title("Número de soldados convocados")
else:
    ax.set_title("Gastos do governo dos EUA")

st.pyplot(fig)
