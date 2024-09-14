import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples.")
    email = st.text_input("Campo de texto para inserção do email do vendedor.")
    data = st.date_input("Campo para selecionar a data de quando foi efetuada a venda.", datetime.now())
    hora = st.time_input("Campo para selecionar a hora de quando foi efetuada a venda.", value=time(9,0))
    valor = st.number_input("Campo numérico para inserir o valor da venda.", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos.", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido.", options=["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"])

    if st.button("Salvar"):
        
        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )

            st.write(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")




if __name__=="__main__":
    main()