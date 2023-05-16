import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# escrevendo um título na página
st.title('Análise de Dados: evolução nos números da educação superior a distância')

#LEITURA DOS ARQUIVOS DE DADOS
df_cursos_2021 = pd.read_parquet('2021.parquet')
df_cursos_2020 = pd.read_parquet('2020.parquet')
df_cursos_2019 = pd.read_parquet('2019.parquet')
df_cursos_2018 = pd.read_parquet('2018.parquet')
df_cursos_2017 = pd.read_parquet('2017.parquet')


#REALIZANDO QUERY PARA FILTRAR APENAS OS DADOS NECESSÁRIOS PARA ANALISE
df_cursos_ead_2021 = df_cursos_2021.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2020 = df_cursos_2020.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2019 = df_cursos_2019.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2018 = df_cursos_2018.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2017 = df_cursos_2017.query('TP_MODALIDADE_ENSINO == 2')

#TRATAMENTO DE DADOS NUMERICOS PARA CATEGORICOS
def data_transformation(df):
    df['TP_ORGANIZACAO_ACADEMICA'] = df['TP_ORGANIZACAO_ACADEMICA'].map({1: 'Universidade',
                                                                        2:'Centro Universitário',
                                                                        3: 'Faculdade',
                                                                        4: 'Instituto Federal de Educação, Ciência e Tecnologia',
                                                                        5: 'Centro Federal de Educação Tecnológica'},na_action=None)

    df['TP_CATEGORIA_ADMINISTRATIVA'] = df['TP_CATEGORIA_ADMINISTRATIVA'].map({
                                                                        1: 'Pública Federal',
                                                                        2: 'Pública Estadual',
                                                                        3: 'Pública Municipal',
                                                                        4: 'Privada com fins lucrativos',
                                                                        5: 'Privada sem fins lucrativos',
                                                                        6: 'Privada - Particular em sentido estrito',
                                                                        7: 'Especial',
                                                                        8: 'Privada comunitária',
                                                                        9: 'Privada confessional'}, na_action=None)

    df['TP_REDE'] = df['TP_REDE'].map({
                                1: 'Pública',
                                2: 'Privada'}, na_action=None)  

    df['TP_GRAU_ACADEMICO'] = df['TP_GRAU_ACADEMICO'].map({
                                                    1: 'Bacharelado',
                                                    2: 'Licenciatura',
                                                    3: 'Tecnológico',
                                                    4: 'Bacharelado e Licenciatura'}, na_action=None)

    df['TP_MODALIDADE_ENSINO'] = df['TP_MODALIDADE_ENSINO'].map({
                                                            1: 'Presencial',
                                                            2: 'Curso a distância'}, na_action=None)

    return df

df_cursos_ead_2021 = data_transformation(df_cursos_ead_2021)
df_cursos_ead_2020 = data_transformation(df_cursos_ead_2020)
df_cursos_ead_2019 = data_transformation(df_cursos_ead_2019)
df_cursos_ead_2018 = data_transformation(df_cursos_ead_2018)
df_cursos_ead_2017 = data_transformation(df_cursos_ead_2017)

#RESUMO DOS DADOS PARA EXIBICAO EM TABELA
dicionario_soma_anos =  {'Ano': [2017, 2018, 2019, 2020, 2021],
                'Alunos ingressantes': [df_cursos_ead_2017['QT_ING'].sum(),
                                        df_cursos_ead_2018['QT_ING'].sum(),
                                        df_cursos_ead_2019['QT_ING'].sum(),
                                        df_cursos_ead_2020['QT_ING'].sum(), 
                                        df_cursos_ead_2021['QT_ING'].sum()], 
               'Alunos Matriculados': [df_cursos_ead_2017['QT_MAT'].sum(),
                                       df_cursos_ead_2018['QT_MAT'].sum(),
                                       df_cursos_ead_2019['QT_MAT'].sum(),
                                       df_cursos_ead_2020['QT_MAT'].sum(),
                                       df_cursos_ead_2021['QT_MAT'].sum()], 
               'Alunos concluintes': [df_cursos_ead_2017['QT_CONC'].sum(),
                                      df_cursos_ead_2018['QT_CONC'].sum(),
                                      df_cursos_ead_2019['QT_CONC'].sum(),
                                      df_cursos_ead_2020['QT_CONC'].sum(), 
                                      df_cursos_ead_2021['QT_CONC'].sum()]
              }


#CRIANDO TABELA PARA EXIBIÇÃO NA APLICAÇÃO
df_soma = pd.DataFrame(dicionario_soma_anos)

grafico_dados_ingressantes = {'Ingressantes':[df_cursos_ead_2017['QT_ING'].sum(),
                              df_cursos_ead_2018['QT_ING'].sum(),
                              df_cursos_ead_2019['QT_ING'].sum(),
                              df_cursos_ead_2020['QT_ING'].sum(),
                              df_cursos_ead_2021['QT_ING'].sum()]}

grafico_dados_concluintes = {'Concluintes':[df_cursos_ead_2017['QT_CONC'].sum(),
                              df_cursos_ead_2018['QT_CONC'].sum(),
                              df_cursos_ead_2019['QT_CONC'].sum(),
                              df_cursos_ead_2020['QT_CONC'].sum(),
                              df_cursos_ead_2021['QT_CONC'].sum()]}

grafico_dados_matriculados = {'Matriculados': [df_cursos_ead_2017['QT_MAT'].sum(),
                                       df_cursos_ead_2018['QT_MAT'].sum(),
                                       df_cursos_ead_2019['QT_MAT'].sum(),
                                       df_cursos_ead_2020['QT_MAT'].sum(),
                                       df_cursos_ead_2021['QT_MAT'].sum()]}
                              

st.header('Tabela de resumo geral')
st.dataframe(data = df_soma, use_container_width=True)
st.header('')
st.header('Resumo gráfico geral')
col1, col2, col3 = st.columns(3, gap='large')
with col1:
    st.header('Ingressantes')
    st.line_chart(grafico_dados_ingressantes)

with col2:
    st.header('Matrículas')
    st.line_chart(grafico_dados_matriculados)

with col3:
    st.header('Concluintes')
    st.line_chart(grafico_dados_concluintes)

#CRIANDO DFS POR AREA DE CURSO
area_negocios_2021 = df_cursos_ead_2021.query("NO_CINE_AREA_GERAL == 'Negócios, administração e direito'")
area_negocios_2017 = df_cursos_ead_2017.query("NO_CINE_AREA_GERAL == 'Negócios, administração e direito'")

area_educacao_2021 = df_cursos_ead_2021.query("NO_CINE_AREA_GERAL == 'Educação'")
area_educacao_2017 = df_cursos_ead_2017.query("NO_CINE_AREA_GERAL == 'Educação'")

area_engenharia_2021 = df_cursos_ead_2021.query("NO_CINE_AREA_GERAL == 'Engenharia, produção e construção'")
area_engenharia_2017 = df_cursos_ead_2017.query("NO_CINE_AREA_GERAL == 'Engenharia, produção e construção'")

area_computacao_2021 = df_cursos_ead_2021.query("NO_CINE_AREA_GERAL == 'Computação e Tecnologias da Informação e Comunicação (TIC)'")
area_computacao_2017 = df_cursos_ead_2017.query("NO_CINE_AREA_GERAL == 'Computação e Tecnologias da Informação e Comunicação (TIC)'")

area_saude_2021 = df_cursos_ead_2021.query("NO_CINE_AREA_GERAL == 'Saúde e bem-estar'")
area_saude_2017 = df_cursos_ead_2017.query("NO_CINE_AREA_GERAL == 'Saúde e bem-estar'")

#CRIANDO GRAFICO INGRESSANTES
n_groups = 5
ing_2021 = [area_negocios_2021['QT_ING'].sum(), 
              area_educacao_2021['QT_ING'].sum(),
              area_engenharia_2021['QT_ING'].sum(),
              area_computacao_2021['QT_ING'].sum(),
              area_saude_2021['QT_ING'].sum()]

ing_2017 = [area_negocios_2017['QT_ING'].sum(), 
              area_educacao_2017['QT_ING'].sum(),
              area_engenharia_2017['QT_ING'].sum(),
              area_computacao_2017['QT_ING'].sum(),
              area_saude_2017['QT_ING'].sum()]


barWidth = 0.25
plt.figure(figsize=(10,5))

r1 = np.arange(len(ing_2021))
r2 = [x + barWidth for x in r1]

plt.bar(r1, ing_2021, color = '#6A5ACD', width=barWidth, label='2021')
plt.bar(r2, ing_2017, color = '#6495ED', width=barWidth, label='2017')

plt.xticks([r + barWidth for r in range(len(ing_2021))], ['Negócios', 
                               'Educação', 
                               'Engenharia', 
                              'Computação', 
                               'Saúde'])
plt.yticks([])

plt.legend(loc="upper right")

figura = plt.show()

st.header('Ingressantes por área do curso')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(figura)

#CRIANDO GRAFICO MATRICULAS
n_groups = 5
mat_2021 = [area_negocios_2021['QT_MAT'].sum(), 
              area_educacao_2021['QT_MAT'].sum(),
              area_engenharia_2021['QT_MAT'].sum(),
              area_computacao_2021['QT_MAT'].sum(),
              area_saude_2021['QT_MAT'].sum()]

mat_2017 = [area_negocios_2017['QT_MAT'].sum(), 
              area_educacao_2017['QT_MAT'].sum(),
              area_engenharia_2017['QT_MAT'].sum(),
              area_computacao_2017['QT_MAT'].sum(),
              area_saude_2017['QT_MAT'].sum()]


barWidth = 0.25
plt.figure(figsize=(10,5))

r1 = np.arange(len(mat_2021))
r2 = [x + barWidth for x in r1]

plt.bar(r1, mat_2021, color = '#6A5ACD', width=barWidth, label='2021')
plt.bar(r2, mat_2017, color = '#6495ED', width=barWidth, label='2017')

plt.xticks([r + barWidth for r in range(len(mat_2021))], ['Negócios', 
                               'Educação', 
                               'Engenharia', 
                              'Computação', 
                               'Saúde'])
plt.yticks([])

plt.legend(loc="upper right")

figura = plt.show()

st.header('')
st.header('Matriculas por área do curso')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(figura)

#CRIANDO GRAFICO CONCLUINTES
n_groups = 5
conc_2021 = [area_negocios_2021['QT_MAT'].sum(), 
              area_educacao_2021['QT_MAT'].sum(),
              area_engenharia_2021['QT_MAT'].sum(),
              area_computacao_2021['QT_MAT'].sum(),
              area_saude_2021['QT_MAT'].sum()]

conc_2017 = [area_negocios_2017['QT_MAT'].sum(), 
              area_educacao_2017['QT_MAT'].sum(),
              area_engenharia_2017['QT_MAT'].sum(),
              area_computacao_2017['QT_MAT'].sum(),
              area_saude_2017['QT_MAT'].sum()]


barWidth = 0.25
plt.figure(figsize=(10,5))

r1 = np.arange(len(conc_2021))
r2 = [x + barWidth for x in r1]

plt.bar(r1, conc_2021, color = '#6A5ACD', width=barWidth, label='2021')
plt.bar(r2, conc_2017, color = '#6495ED', width=barWidth, label='2017')

plt.xticks([r + barWidth for r in range(len(conc_2021))], ['Negócios', 
                               'Educação', 
                               'Engenharia', 
                              'Computação', 
                               'Saúde'])
plt.yticks([])

plt.legend(loc="upper right")

figura = plt.show()

st.header('')
st.header('Concluintes por área do curso')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(figura)