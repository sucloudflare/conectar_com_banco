from google.colab import files
from google.cloud import bigquery
from google.colab import auth

#Autenticar no Google Cloud
auth.authenticate_user()

#Criando o client do BigQuery
client = bigquery.Client()

#Definir o id do projeto
project_id = 'projeto-edson-443513'
table_id = 'projeto-edson-443513_faculdade_aluno' #id_projeto.nome_dataset.nome_tabela ou o conjunto de tabela e tabela

#Enviando o Dataframe para o BigQuery
df.to_gbq(projeto-edson-443513, project_id=project_id, if_exists='replace')