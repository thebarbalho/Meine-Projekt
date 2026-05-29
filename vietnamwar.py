import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Guerra do Vietnã", layout="centered")
st.title("Guerra do Vietnã - Análise de Dados sobre os Estados Unidos da América")

arquivo = "vietnamwar.xlsx"

try:
    xls = pd.ExcelFile(arquivo)
except Exception as e:
    st.error(f"Erro ao abrir arquivo: {e}")
    st.stop()

aba = st.selectbox("Escolha o conjunto de dados:", xls.sheet_names)

df = pd.read_excel(arquivo, sheet_name=aba)

st.subheader("Dados")
st.dataframe(df)

fig, ax = plt.subplots(figsize=(10, 5))

x = df.iloc[:, 0].astype(str)
y = pd.to_numeric(df.iloc[:, 1], errors='coerce')
indices = range(len(x))

if "Baixas" in aba:
    ax.plot(indices, y, marker='o')
    ax.set_title("Baixas nas Forças Armadas dos EUA")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Número de Mortes")

elif "Convocados" in aba:
    ax.bar(indices, y)
    ax.set_title("Total de Convocados por Ano")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Soldados Convocados")

ax.set_xticks(indices)
ax.set_xticklabels(x, rotation=45)
ax.ticklabel_format(style='plain', axis='y')
fig.tight_layout()

st.pyplot(fig)
