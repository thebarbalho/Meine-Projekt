import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Guerra do Vietnã",
    layout="centered"
)

st.title("Guerra do Vietnã - Análise de Dados sobre os Estados Unidos da América")

arquivo = "vietnamwar.xlsx"

xls = pd.ExcelFile(arquivo)

aba = st.selectbox(
    "Escolha o conjunto de dados:",
    xls.sheet_names
)

df = pd.read_excel(arquivo, sheet_name=aba)

st.subheader("Dados")
st.dataframe(df)

fig, ax = plt.subplots(figsize=(10, 5))

if "Baixas" in aba:
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    ax.plot(x, y, marker='o')
    ax.set_title("Baixas nas Forças Armadas dos EUA")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Número de Mortes")

elif "Convocados" in aba:
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    ax.bar(x, y)
    ax.set_title("Total de Convocados por Ano")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Soldados Convocados")

elif "Gastos" in aba:
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    ax.plot(x, y, marker='o')
    ax.set_title("Gastos do Governo dos EUA")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Valor em bilhões de dólares")
    ax.ticklabel_format(style='plain', axis='y')

st.pyplot(fig)
