import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Área Pix - Banco do Tchelo", page_icon="💸", layout="centered")

st.title("💸 Área Pix — Banco do Tchelo")
st.write("Transferências instantâneas seguras.")
st.write("---")

if "saldo" not in st.session_state:
    st.session_state.saldo = 2500.00

st.info(f"Saldo disponível: R$ {st.session_state.saldo:,.2f}")

with st.form("form_pix", clear_on_submit=True):
    nome = st.text_input("Nome do Favorecido:")
    valor_txt = st.text_input("Valor da Transferência (R$):", placeholder="Ex: 150,00")
    submit = st.form_submit_button("TRANSFERIR AGORA", use_container_width=True)

if submit:
    try:
        valor = float(valor_txt.replace(",", "."))
        if valor <= 0:
            raise ValueError
    except ValueError:
        st.error("Informe um valor válido maior que zero.")
        valor = None

    if valor:
        if valor > st.session_state.saldo:
            st.error("❌ Saldo insuficiente.")
        else:
            st.session_state.saldo -= valor
            agora = datetime.now().strftime("%d/%m/%Y %H:%M")
            st.session_state.extrato.append({
                "data": agora,
                "tipo": f"Pix para {nome}",
                "valor": -valor
            })
            st.success("✅ Pix realizado com sucesso!")
            st.balloons()
