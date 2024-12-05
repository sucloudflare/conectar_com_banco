# Instalar a biblioteca pyodbc, necessária para conectar e interagir com o banco de dados SQL Server
!pip install pyodbc

# Importando as bibliotecas necessárias
import pyodbc  # Biblioteca para conexão com SQL Server
import pandas as pd  # Biblioteca para manipulação de dados

# Configuração dos parâmetros de conexão com o banco de dados SQL Server
server = '34.172...'  # IP público do servidor SQL Server
database = 'meu_banco'     # Nome do banco de dados SQL Server
username = 'sa'            # Nome de usuário para autenticação
password = '1234'          # Senha correspondente ao usuário

# Estabelecendo a conexão com o banco de dados SQL Server
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)

# Criando um cursor para executar consultas SQL no banco de dados
cursor = conn.cursor()

# Definindo a consulta SQL que será executada
query = '''
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';
'''  # Consulta SQL para listar tabelas do banco de dados SQL Server

# Executando a consulta SQL e armazenando os resultados em um DataFrame do pandas
tabelas = pd.read_sql_query(query, conn)

# Exibindo as informações das tabelas no banco de dados
from IPython.display import display  # Para exibir de forma amigável em notebooks
display(tabelas)

# Fechando o cursor após concluir a execução da consulta
cursor.close()

# Fechando a conexão com o banco de dados para liberar recursos
conn.close()
