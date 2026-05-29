import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("Guerra do Vietnã")

arquivo = "vietnamwar.xlsx.xlsx"

# Carrega Excel
xls = pd.ExcelFile(arquivo)

aba = st.selectbox("Escolha a aba:", xls.sheet_names)

# Ler dados
df = pd.read_excel(xls, sheet_name=aba)

st.write(df)

# Gráfico
fig, ax = plt.subplots()

x = df.iloc[:, 0]
y = df.iloc[:, 1]

ax.plot(x, y, marker='o')
ax.set_title(aba)

st.pyplot(fig)
