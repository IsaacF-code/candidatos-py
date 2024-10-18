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

    unidade_eleitoral = base['NM_UE'].unique()

    unidade_selecionada = st.sidebar.selectbox(
        "Selecione uma unidade eleitoral(NM_UE)",
        unidade_eleitoral,
        index=None,
        placeholder="Selecione uma unidade eleitoral"
    )

    cargo = base['DS_CARGO'].unique()

    cargo_selecionado = st.sidebar.selectbox(
        "Selecione um Cargo (DS_CARGO)",
        cargo,
        index=None,
        placeholder="Selecione um cargo"
    )


    # st.write(base_filtrada)

    st.header("Distribuição do Grau de Instrução")

    st.write("Distribuição por Grau de Instrução")

    base_filtrada = base[
        (base['NM_UE'] == unidade_selecionada) & (base['DS_CARGO'] == cargo_selecionado)
    ]
    grau_instrucao = base_filtrada['DS_GRAU_INSTRUCAO'].value_counts().reset_index()
    grau_instrucao.columns = ['DS_GRAU_INSTRUCAO', 'Quantidade']

    st.bar_chart(grau_instrucao.set_index('DS_GRAU_INSTRUCAO')['Quantidade'], x_label='DS_GRAU_INSTRUCAO', y_label='COUNT')

    st.header("Relação entre Gênero e Grau de Instrução")

    st.write("Grau de Instrução por Gênero")

    st.bar_chart(grau_instrucao.set_index('DS_GRAU_INSTRUCAO')['Quantidade'], x_label='DS_GRAU_INSTRUCAO', y_label='COUNT', color=base('DS_GENERO'), stack=False)
