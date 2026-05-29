import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Guerra do Vietnã",
    layout="centered"
)

st.title("Guerra do Vietnã - Análise de Dados sobre os Estados Unidos da América")

# NOME DO ARQUIVO
arquivo = "vietnamwar.xlsx.xlsx"

# LER EXCEL
xls = pd.ExcelFile(arquivo)

# ESCOLHER ABA
aba = st.selectbox(
    "Escolha o conjunto de dados:",
    xls.sheet_names
)

# LER DADOS
df = pd.read_excel(arquivo, sheet_name=aba)

# MOSTRAR TABELA
st.subheader("Dados")
st.dataframe(df)

# CRIAR GRÁFICO
fig, ax = plt.subplots(figsize=(10,5))

# =========================
# GRÁFICO DE BAIXAS
# =========================
if "Baixas" in aba:

    x = df.iloc[:,0]
    y = df.iloc[:,1]

    ax.plot(x, y, marker='o')

    ax.set_title("Baixas nas Forças Armadas dos EUA")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Número de Mortes")

# =========================
# GRÁFICO DE CONVOCADOS
# =========================
elif "Convocados" in aba:

    x = df.iloc[:,0]
    y = df.iloc[:,1]

    ax.bar(x, y)

    ax.set_title("Total de Convocados por Ano")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Soldados Convocados")

# =========================
# GRÁFICO DE GASTOS
# =========================
elif "Gastos" in aba:

    x = df.iloc[:,0]
    y = df.iloc[:,1]

    ax.plot(x, y, marker='o')

    ax.set_title("Gastos do Governo dos EUA")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Valor em bilhões de dólares")

    # melhora visual dos números
    ax.ticklabel_format(style='plain', axis='y')

# EXIBIR
st.pyplot(fig)
