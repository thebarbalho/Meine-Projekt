import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Guerra do Vietnã", layout="centered")
st.title("Análise de Dados sobre os Estados Unidos da América durante a Guerra do Vietnã (1955-1975)")

arquivo = "vietnamwar.xlsx"

try:
    xls = pd.ExcelFile(arquivo)
except FileNotFoundError:
    st.error(f"Arquivo '{arquivo}' não encontrado. Coloque o arquivo na mesma pasta do app.")
    st.stop()

aba = st.selectbox("Escolha a aba do arquivo:", xls.sheet_names)

df = pd.read_excel(arquivo, sheet_name=aba)

st.subheader("Dados")
st.dataframe(df)

colunas = df.columns.tolist()
colunas_num = df.select_dtypes(include='number').columns.tolist()

eixo_x = st.selectbox("Coluna para eixo X:", colunas, index=0)

colunas_y = colunas_num if colunas_num else colunas
eixo_y = st.selectbox("Coluna para eixo Y:", colunas_y, index=min(1, len(colunas_y) - 1))

tipo = st.selectbox("Tipo de gráfico:", ["Linha", "Barras", "Dispersão", "Área"])

fig, ax = plt.subplots(figsize=(10, 5))

if tipo == "Linha":
    ax.plot(df[eixo_x], df[eixo_y], marker='o')
elif tipo == "Barras":
    ax.bar(df[eixo_x], df[eixo_y])
elif tipo == "Dispersão":
    ax.scatter(df[eixo_x], df[eixo_y])
elif tipo == "Área":
    ax.fill_between(df[eixo_x].astype(float), df[eixo_y].astype(float), alpha=0.5)
    ax.plot(df[eixo_x], df[eixo_y], marker='o')

ax.set_xlabel(eixo_x)
ax.set_ylabel(eixo_y)
ax.set_title(f"{tipo} - {eixo_y} por {eixo_x}")
ax.ticklabel_format(style='plain', axis='y')

st.pyplot(fig)
