import pandas as pd

#SCRIPT PARA TRATAMENTO DOS DADOS COLETADOS
df_cursos_2021 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2021.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2020 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2020.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2019 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2019.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2018 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2018.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2017 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2017.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)

used_columns = [
    'NU_ANO_CENSO',
    'TP_ORGANIZACAO_ACADEMICA',
    'TP_CATEGORIA_ADMINISTRATIVA',
    'TP_REDE', 
    'NO_CINE_AREA_GERAL',
    'TP_GRAU_ACADEMICO',
    'TP_MODALIDADE_ENSINO',
    'QT_CURSO',
    'QT_VG_TOTAL',
    'QT_VG_TOTAL_EAD',
    'QT_INSCRITO_TOTAL',
    'QT_INSCRITO_TOTAL_EAD',
    'QT_ING',
    'QT_MAT',
    'QT_CONC',
    'QT_SIT_TRANCADA',
    'QT_SIT_DESVINCULADO',
    'QT_SIT_TRANSFERIDO'
]

df_cursos_2021.to_parquet('2021.parquet')
df_cursos_2020.to_parquet('2020.parquet')
df_cursos_2019.to_parquet('2019.parquet')
df_cursos_2018.to_parquet('2018.parquet')
df_cursos_2017.to_parquet('2017.parquet')