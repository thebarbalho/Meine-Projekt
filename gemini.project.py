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

def app():
    st.title("Consulte ao Gemini")

    pergunta = st.text_input("Digite o seu pedido:")

    if st.button("Enviar"):
        if pergunta:
            with st.spinner("Pensando..."):
                resposta = model.generate_content(pergunta)
                st.success(resposta.text)
        else:
            st.warning("Formule um pedido melhor")
