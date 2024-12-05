<h1>Guia de Conexão e Configuração para PostgreSQL, MySQL, SQL Server e BigQuery</h1>
<p>Este guia fornece instruções detalhadas para configurar conexões a bancos de dados, criar bancos de dados, importar arquivos e trabalhar com ferramentas como Google Colab, Workbench e Cloud Storage.</p>

<h2>Pré-requisitos</h2>
<p>Antes de começar, você precisará:</p>
<ul>
<li>Uma conta na plataforma em nuvem (Google Cloud ou outro).</li>
  <li>Ferramentas instaladas em sua máquina local:
  <ul>
    <li>Python 3.x (com bibliotecas como <code>psycopg2</code>, <code>mysql-connector-python</code>, <code>pyodbc</code>, <code>pandas</code>, <code>google-cloud-bigquery</code>).</li>
  <li>Workbench apropriado para cada banco de dados (pgAdmin, MySQL Workbench, Azure Data Studio).</li>
  <li>Google Cloud SDK (para BigQuery e Cloud Storage).</li>
<li>Permissões de rede para conexão externa (liberar IPs no firewall, configurar VPCs).</li>
</ul>
</li>
  </ul>

  <h2>Etapa 1: Configuração de Rede para Acessar Bancos de Dados</h2>
  <h3>Google Cloud:</h3>
    <ol>
   <li>Vá até <strong>VPC Network &gt; Firewall Rules</strong> no console do Google Cloud.</li>
  <li>Crie uma regra para permitir conexões de entrada na porta:
 <ul>
   <li>PostgreSQL: <code>5432</code></li>
   <li>MySQL: <code>3306</code></li>
  <li>SQL Server: <code>1433</code></li>
  </ul>
 </li>
  <li>Use o IP público da sua máquina local ou configure para permitir qualquer IP temporariamente (<code>0.0.0.0/0</code>).</li>
    </ol>

  <h3>Conexão do Colab:</h3>
  <ul>
  <li>Certifique-se de que o Colab tenha acesso à internet.</li>
 <li>Adicione a biblioteca necessária no início do código (<code>!pip install ...</code>).</li>
  </ul>

<h3>Conexão do Workbench:</h3>
<ul>
        <li>No Workbench escolhido, use o IP do banco de dados no Google Cloud e configure o usuário, senha e porta.</li>
</ul>

<h2>Etapa 2: Criando um Banco de Dados</h2>
<h3>PostgreSQL</h3>
<pre><code>CREATE DATABASE meu_banco;</code></pre>

<h3>MySQL</h3>
<pre><code>CREATE DATABASE meu_banco;</code></pre>

<h3>SQL Server</h3>
<pre><code>CREATE DATABASE meu_banco;</code></pre>

<h3>BigQuery</h3>
<ol>
<li>Acesse o console do Google Cloud.</li>
<li>No BigQuery, clique em "Criar Conjunto de Dados" e preencha as informações necessárias.</li>
<li>O conjunto de dados será equivalente a um banco de dados.</li>
</ol>

<h2>Etapa 3: Importando Arquivos CSV ou SQL</h2>
<h3>Carregar Arquivo no Google Cloud Storage</h3>
  <ol>
<li>Vá para <strong>Storage &gt; Buckets</strong>.</li>
 <li>Faça upload do arquivo CSV ou SQL.</li>
 <li>Use o caminho do arquivo no Google Cloud Storage (<code>gs://bucket-name/file-name.csv</code>).</li>
 </ol>
<h3>Importando CSV</h3>
<h4>PostgreSQL:</h4>
<pre><code>COPY table_name
FROM 'gs://bucket-name/file.csv'
DELIMITER ','
CSV HEADER;</code></pre>
<h4>MySQL:</h4>
<pre><code>LOAD DATA INFILE 'gs://bucket-name/file.csv'
INTO TABLE table_name
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;</code></pre>

<h4>SQL Server:</h4>
    <pre><code>BULK INSERT table_name
FROM 'gs://bucket-name/file.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);</code></pre>
<h4>BigQuery:</h4>
    <p>No console do BigQuery, clique em <strong>Criar Tabela</strong> e selecione o arquivo no Storage.</p>

<h3>Executando Arquivos SQL</h3>
    <pre><code>\i 'path/to/file.sql'; -- PostgreSQL
SOURCE 'path/to/file.sql'; -- MySQL
EXEC ('path/to/file.sql'); -- SQL Server</code></pre>

<h2>Etapa 4: Conectar no Colab</h2>
<h3>PostgreSQL</h3>
    <pre><code>!pip install psycopg2
import psycopg2

conn = psycopg2.connect(
    host="IP_DO_POSTGRES",
    database="meu_banco",
    user="usuario",
    password="senha"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela;")
print(cursor.fetchall())</code></pre>

<h3>MySQL</h3>
    <pre><code>!pip install mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
    host="IP_DO_MYSQL",
    database="meu_banco",
    user="usuario",
    password="senha"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela;")
print(cursor.fetchall())</code></pre>

<h3>SQL Server</h3>
    <pre><code>!pip install pyodbc
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IP_DO_SQLSERVER;'
    'DATABASE=meu_banco;'
    'UID=usuario;'
    'PWD=senha;'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela;")
print(cursor.fetchall())</code></pre>

<h3>BigQuery</h3>
    <pre><code>!pip install google-cloud-bigquery
from google.cloud import bigquery

client = bigquery.Client()
query = "SELECT * FROM `projeto-dataset.tabela`"
df = client.query(query).to_dataframe()
print(df)</code></pre>

<h2>Etapa 5: Conexão ao Workbench</h2>
<p>Abra o Workbench apropriado para o banco de dados. Configure os parâmetros (IP, porta, usuário, senha) e conecte-se.</p>

<h2>Recursos Úteis</h2>
<ul>
<li><a href="https://cloud.google.com/sdk" target="_blank">Google Cloud SDK</a></li>
<li><a href="https://pandas.pydata.org/docs/" target="_blank">Pandas Documentation</a></li>
<li><a href="https://www.psycopg.org/docs/" target="_blank">psycopg2 Documentation</a></li>
<li><a href="https://dev.mysql.com/doc/connector-python/en/" target="_blank">MySQL Connector Documentation</a></li>
<li><a href="https://github.com/mkleehammer/pyodbc" target="_blank">PyODBC Documentation</a></li>
</ul>
