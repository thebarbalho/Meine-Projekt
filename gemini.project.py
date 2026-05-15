import streamlit as st
from google import genai

# SENHAS DE ACESSO AO APP

GEMINI_API_KEY= 'AIzaSyBJRSrbzvLVO7NIs7irPm1VCCebE6Lq9zE'
APP_PASSWORD=2908

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
