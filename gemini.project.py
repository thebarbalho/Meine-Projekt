import streamlit as st

# SENHAS DE ACESSO AO APP

GEMINI_API_KEY= AIzaSyBJRSrbzvLVO7NIs7irPm1VCCebE6Lq9zE
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

# PERGUNTA AO GEMINI

from IPython.display import HTML, Markdown

model = genai.GenerativeModel(MODEL_ID)

resposta = model.generate_content(
    contents='?',
)
# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {resposta.text}"))
