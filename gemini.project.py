import streamlit as st
from google import genai

# ACESSO AO PROGRAMA

GEMINI_API_KEY= 'AIzaSyBJRSrbzvLVO7NIs7irPm1VCCebE6Lq9zE'
APP_PASSWORD= "2908"

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

def login():
    st.title("LOGIN NO APP")

    senha = st.text_input("Digite a senha:", type="password")

    if st.button("Entrar"):
        if senha == APP_PASSWORD:
            st.session_state.autenticado = True
        else:
            st.error("Senha incorreta!")

if not st.session_state.autenticado:
    login()
else:
    st.write("Você está logado!")

# PERGUNTA AO GEMINI

from IPython.display import HTML, Markdown

model = genai.GenerativeModel(MODEL_ID)

resposta = model.generate_content(
    contents=st.write
)
# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {resposta.text}"))
