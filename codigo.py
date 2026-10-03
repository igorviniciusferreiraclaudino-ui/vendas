#Importantes
import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path
pasta = Path(__file__).parent
caminho = pasta/'vendas.csv'

tabela = pd.read_csv(caminho)
#titulo
st.write('# Sistema de Vendas')

#seção de cadastro de vendas
st.sidebar.write('## Cadastrar Vendas')
    #campo data
data = st.sidebar.date_input('Data', min_value='2026-10-01', max_value='today')
    #campo vendedor
vendedor = st.sidebar.text_input('Vendedor')
    #campo produto
produto = st.sidebar.text_input('Produto')
    #campo quantidade
qtd = st.sidebar.number_input('Quantidade', step=1)
    #campo valor
valor = st.sidebar.number_input('Valor')
    #botão de cadastrar vendas
botao = st.sidebar.button('Cadastrar Venda')
        #botão funcional
if botao:
    if valor <= 0 or qtd == 0 or vendedor == '':
        st.warning('Por favor, preencha todas as informações')
    else:
        nova_venda = [data, vendedor, produto, qtd, valor]
        linhafinal = len(tabela)
        tabela.loc[linhafinal] = nova_venda
        tabela.to_csv(caminho, index=False)
        st.success('Venda Cadastrada')
#seção de vendas cadastradas
st.write('## Vendas Cadastradas')
    #tabela  com as vendas
st.dataframe(tabela)
#seção dashboard
st.write('## dashboard')
    #faturamento total
faturamento = (tabela['valor']).sum()
st.metric('faturamento total', f'R${faturamento}')

    #grafico de barras
grafico1 = px.bar(tabela, x='vendedor', y ='valor', color='produto')
st.plotly_chart(grafico1)
    #grafico de pizzas
grafico2 = px.pie(tabela, names='produto', values='valor')
st.plotly_chart(grafico2)
grafico3 = px.pie(tabela, names='produto', values='valor', hole=0.3)
st.plotly_chart(grafico3)
