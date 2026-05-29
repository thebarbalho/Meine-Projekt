import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Guerra do Vietnã", layout="centered")
st.title("Guerra do Vietnã - Análise de Dados")

# ============================
# TESTE: gráfico simples para verificar se matplotlib funciona
# ============================
st.subheader("Teste - Gráfico de exemplo")
fig_teste, ax_teste = plt.subplots()
ax_teste.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o')
ax_teste.set_title("Teste - gráfico está funcionando")
st.pyplot(fig_teste)
# ============================

arquivo = "vietnamwar.xlsx"

try:
    xls = pd.ExcelFile(arquivo)
except Exception as e:
    st.error(f"Erro ao abrir arquivo: {e}")
    st.stop()

aba = st.selectbox("Escolha a aba do arquivo:", xls.sheet_names)

df = pd.read_excel(arquivo, sheet_name=aba)

st.subheader("Dados")
st.dataframe(df)
st.write("Colunas encontradas:", df.columns.tolist())
st.write("Tipos dos dados:")
st.write(df.dtypes)

colunas = df.columns.tolist()
colunas_num = df.select_dtypes(include='number').columns.tolist()

eixo_x = st.selectbox("Coluna para eixo X:", colunas, index=0)
eixo_y = st.selectbox("Coluna para eixo Y:", colunas_num if colunas_num else colunas, index=min(1, len(colunas) - 1))
tipo = st.selectbox("Tipo de gráfico:", ["Linha", "Barras", "Dispersão", "Área"])

st.write(f"Gerando gráfico: X={eixo_x}, Y={eixo_y}, Tipo={tipo}")

fig, ax = plt.subplots(figsize=(10, 5))

x_vals = pd.to_numeric(df[eixo_x], errors='ignore')
y_vals = pd.to_numeric(df[eixo_y], errors='coerce')

if tipo == "Linha":
    ax.plot(x_vals, y_vals, marker='o')
elif tipo == "Barras":
    ax.bar(x_vals, y_vals)
elif tipo == "Dispersão":
    ax.scatter(x_vals, y_vals)
elif tipo == "Área":
    ax.fill_between(range(len(y_vals)), y_vals, alpha=0.5)
    ax.plot(x_vals, y_vals, marker='o')
    ax.set_xticks(range(len(x_vals)))
    ax.set_xticklabels(x_vals, rotation=45)

ax.set_xlabel(eixo_x)
ax.set_ylabel(eixo_y)
ax.set_title(f"{tipo} - {eixo_y} por {eixo_x}")
ax.ticklabel_format(style='plain', axis='y')
fig.tight_layout()

st.pyplot(fig)
