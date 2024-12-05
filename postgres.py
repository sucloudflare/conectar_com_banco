# Instalar a biblioteca psycopg2, necessária para conectar e interagir com o banco de dados PostgreSQL
!pip install psycopg2

# Importando as bibliotecas necessárias
import psycopg2  # Biblioteca para conexão com PostgreSQL
import pandas as pd  # Biblioteca para manipulação de dados

# Configuração dos parâmetros de conexão com o banco de dados PostgreSQL
host = '34.172.140.255'  # IP público da instância do PostgreSQL no Google Cloud
user = 'postgres'         # Nome de usuário para autenticação
password = '0000'         # Senha correspondente ao usuário
database = 'meu-bd'       # Nome do banco de dados PostgreSQL

# Estabelecendo a conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Criando um cursor para executar consultas SQL no banco de dados
cursor = conn.cursor()

# Definindo a consulta SQL que será executada
query = '''
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public'
AND table_type='BASE TABLE';
'''

# Executando a consulta SQL e armazenando os resultados em um DataFrame do pandas
tabelas = pd.read_sql_query(query, conn)

# Exibindo as informações das tabelas no banco de dados
from IPython.display import display  # Para exibir de forma amigável em notebooks
display(tabelas)

# Fechando o cursor após concluir a execução da consulta
cursor.close()

# Fechando a conexão com o banco de dados para liberar recursos
conn.close()
