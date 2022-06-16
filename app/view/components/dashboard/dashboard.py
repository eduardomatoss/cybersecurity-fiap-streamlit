import streamlit as st
import pandas as pd

from app.view.components.sidebar.sidebar import sidebar
from app.service.delivery_api import getAllDeliveryMan, getAllBuyers

def dashboard():

    st.header("Delivery Dashboard")

    st.markdown(""" <style>
                      @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Nunito:wght@300&family=Roboto+Mono:wght@300&display=swap');
                      * {
                          font-family: 'Nunito', sans-serif;
                      }
                      #MainMenu {visibility: hidden;}
                      .css-k0sv6k {visibility: hidden;}
                      .streamlit-expanderHeader {display:none;}
                      .streamlit-expander {border-color: #f2f7ff;}
                      .css-fg4pbf {
                          position: absolute;
                          background: #f2f7ff;
                          color: rgb(49, 51, 63);
                          inset: 0px;
                          overflow: hidden;
                      }
                      .css-1ht1j8u {
                          overflow-wrap: normal;
                          text-overflow: ellipsis;
                          width: 100%;
                          overflow: hidden;
                          white-space: nowrap;
                          font-family: 'Nunito', sans-serif;
                          line-height: normal;
                      }
                      .css-12oz5g7 {
                          flex: 1 1 0%;
                          width: 100%;
                          padding: 6rem 1rem 10rem;
                          max-width: 80rem;
                      }
                      .css-10trblm {
                          position: relative;
                          flex: 1 1 0%;
                          margin-left: calc(3rem);
                          text-align: center;
                        }
                      .css-1l269bu {
                          width: calc(16.6667% - 1rem);
                          flex: 1 1 calc(16.6667% - 1rem);
                          background-color: #FFFFFF;
                          border-radius: 15px;
                          padding: 15px;
                      }
                      .css-115gedg {
                          width: calc(66.6667% - 1rem);
                          flex: 1 1 calc(66.6667% - 1rem);
                          background-color: #FFFFFF;
                          border-radius: 15px;
                          padding: 15px;
                      }
                      .css-1r6slb0 {
                          width: calc(33.3333% - 1rem);
                          flex: 1 1 calc(33.3333% - 1rem);
                          background-color: #FFFFFF;
                          border-radius: 15px;
                          padding: 15px;
                      }
                      .streamlit-expanderContent {
                          position: relative;
                          background-color: #FFF;
                          border-radius: 15px;
                          padding: 15px;
                      }
                      .css-183lzff {
                          font-family: "Source Code Pro", monospace;
                          white-space: pre;
                          font-size: 14px;
                          overflow-x: auto;
                          background-color: rgb(255, 255, 255);
                          padding: 10px;
                          border-radius: 15px;
                      }
                  </style>""", unsafe_allow_html=True)

    sidebar()

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col2.metric("Funcionários", "0", "0%")
    col3.metric("Clientes", "0", "0%")
    col4.metric("Faturamento", "R$ 250k", "R$ 10.000")
    col1.metric("Quantidade Entregas", "230", "45%")
    col5.metric("Entregas Realizadas", "200", "87%")
    col6.metric("Entregas Não Concluídas", "30", "-13%")

    c1, c2 = st.columns((4, 2))

    with c1:
      with st.container():
        d = {"lat": [-23.5215024], "lon": [-46.7069997]}
        df = pd.DataFrame(
        data=d
        )
        st.map(df)

    buyers = getAllBuyers()

    with c2:
      with st.container():
        st.subheader('Últimos Clientes')
        for buyer in buyers:
          st.text(f"{buyer.get('name')}    CPF : {'{}.{}.{}-{}'.format(buyer.get('cpf')[:3], buyer.get('cpf')[3:6], buyer.get('cpf')[6:9], buyer.get('cpf')[9:])}")

    deliveryMens = getAllDeliveryMan()

    for mens in deliveryMens:
      cols1, cols2, cols3 = st.columns((1, 4, 2))
      
      with cols1:
        st.text(f"Funcionário : {mens.get('id')}")

      with cols2:
        st.text(f"Nome Completo : {mens.get('name')}")
        
      with cols3:
        st.text(f"Veículo : {mens.get('vehicle')}")