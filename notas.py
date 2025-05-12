'''
Projeto de integração tabela excel de nf produtos com o banco de dados/
Futuramente tentar integração com api para automatizar com as alterações na planilha
'''

import pandas as pd
import os
from sqlalchemy import create_engine
#Importar as bibliotecas que irei usar incluindo a principal sendo o sqlalchemy que irá fazer a ligação com o postgres

db_name = os.environ['POSTGRES_DB']
db_user = os.environ['POSTGRES_USER']
db_password = os.environ['POSTGRES_PASSWORD']
db_host = os.environ['POSTGRES_HOST']
db_port = os.environ['POSTGRES_PORT']
#Utilizar os dados do env para colocar as informações do banco sem correr o risco do vazamento de dados caso eu suba no github


df = pd.read_excel(r'Caminho do arquivo')
#Transformar o arquivo excel em um dataframe

db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
#Adicionar o caminho do banco de dados e as informações que passei anteriormente

engine = create_engine(db_url)
#Criar a engine do banco de dados

try:
    with engine.connect() as conn:
        df.to_sql('NF_PRODUTOS', con=conn, schema='bronze', if_exists='replace', index=False)
        print("Tabela enviada para 'bronze' com sucesso!")
        #Por fim enviar a tabela para o banco postgres no schema bronze pois os dados ainda não foram tratados
except Exception as e:
    print("Erro ao conectar:", e)
    #Print para o caso de erro