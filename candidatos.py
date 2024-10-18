import streamlit as st
import pandas as pd
from io import StringIO
import plotly.express as px

base_csv = st.file_uploader("Escolha o arquivo CSV com os dados dos candidatos")

if base_csv != None:
    bytes_data = base_csv.getvalue()
    string_data = StringIO(bytes_data.decode("ISO-8859-1"))
    base = pd.read_csv(string_data, sep=';', decimal=',')

    st.header("Prévia dos Dados")
    base

st.sidebar.header("Filtros")

unidade_eleitoral = base.groupby('NM_UE')

st.sidebar.selectbox(
    "Selecione uma unidade eleitoral(NM_UE)",
    unidade_eleitoral,
    index=None
)

cargo = base.groupby('DS_CARGO')

st.sidebar.selectbox(
    "Selecione um Cargo (DS_CARGO)",
    cargo,
    index=None
)

st.header("Distribuição do Grau de Instrução")

st.write("Distribuição por Grau de Instrução")

grau_instrucao = base.groupby('DS_GRAU_INSTRUCAO').agg({'count': 'sum'}).reset_index()

st.bar_chart(grau_instrucao, x='DS_GRAU_INSTRUCAO', y='count')
