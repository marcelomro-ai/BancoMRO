import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Banco do Tchelo", page_icon="🏦", layout="centered")

credentials = {
    'usernames': {
        'tchelo': {
            'name': 'Marcelo Rodrigues',
            'password': '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW'
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    'banco_cookie',
    'banco_signature_key',
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login('Entrar no Banco do Tchelo', 'main')

if authentication_status == False:
    st.error('Usuário ou senha incorretos.')
elif authentication_status == None:
    st.warning('Por favor, digite seu usuário e senha para acessar.')
    st.info("💡 **Dica:** usuário `tchelo` e senha `123`")
elif authentication_status:
    authenticator.logout('Sair da Conta', 'sidebar')

    if "saldo" not in st.session_state:
        st.session_state.saldo = 2500.00
    if "extrato" not in st.session_state:
        st.session_state.extrato = [
            {"data": datetime.now().strftime("%d/%m/%Y %H:%M"), "tipo": "Depósito Inicial", "valor": 2500.00}
        ]

    st.title("🏦 Banco do Tchelo")
    st.metric("Saldo Disponível", f"R$ {st.session_state.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    st.subheader("📄 Extrato de Movimentações")
    st.dataframe(pd.DataFrame(st.session_state.extrato), use_container_width=True)
