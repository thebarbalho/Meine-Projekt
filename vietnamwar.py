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

st.write("Abas encontradas no arquivo:", xls.sheet_names)

aba = st.selectbox(
    "Escolha o conjunto de dados:",
    xls.sheet_names
)

df = pd.read_excel(arquivo, sheet_name=aba)

st.subheader("Dados")
st.dataframe(df)

colunas_numericas = df.select_dtypes(include='number').columns.tolist()

aba_lower = aba.lower()

if "baixa" in aba_lower:
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o')
    ax.set_title("Baixas nas Forças Armadas dos EUA")
    ax.set_xlabel(df.columns[0])
    ax.set_ylabel(df.columns[1])

elif "convoc" in aba_lower:
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x, y)
    ax.set_title("Total de Convocados por Ano")
    ax.set_xlabel(df.columns[0])
    ax.set_ylabel(df.columns[1])

elif "gasto" in aba_lower:
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o')
    ax.set_title("Gastos do Governo dos EUA")
    ax.set_xlabel(df.columns[0])
    ax.set_ylabel(df.columns[1])
    ax.ticklabel_format(style='plain', axis='y')

else:
    st.info("Nenhum padrão conhecido no nome da aba. Configure o gráfico manualmente abaixo.")

    if len(colunas_numericas) >= 1:
        eixo_x = st.selectbox("Coluna para eixo X:", df.columns, index=0)
        eixo_y = st.selectbox("Coluna para eixo Y:", colunas_numericas, index=0)
        tipo_grafico = st.selectbox("Tipo de gráfico:", ["Linha", "Barras", "Dispersão", "Área"])

        fig, ax = plt.subplots(figsize=(10, 5))

        if tipo_grafico == "Linha":
            ax.plot(df[eixo_x], df[eixo_y], marker='o')
        elif tipo_grafico == "Barras":
            ax.bar(df[eixo_x], df[eixo_y])
        elif tipo_grafico == "Dispersão":
            ax.scatter(df[eixo_x], df[eixo_y])
        elif tipo_grafico == "Área":
            ax.fill_between(df[eixo_x].astype(float), df[eixo_y].astype(float), alpha=0.5)
            ax.plot(df[eixo_x], df[eixo_y], marker='o')

        ax.set_xlabel(eixo_x)
        ax.set_ylabel(eixo_y)
        ax.set_title(f"{tipo_grafico} - {eixo_y} por {eixo_x}")
    else:
        st.warning("Não há colunas numéricas para gerar gráfico.")
        fig, ax = plt.subplots()

st.pyplot(fig)
