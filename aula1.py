# importando a biblioteca pandas, para mexer com tabelas
import pandas as pd

# df = dataframe (tabela)
# lendo um csv com o pandas (pd)
df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

# head(X) -> mostrar as X primeiras linhas da tabela
print(
  '===Primeiras 10 linhas da tabela===\n',
  df.head(10)
)

# info() -> faz descrições sobre as colunas da tabela
# muito parecido com o DESC do sql
print('\n===Informações===')
df.info()

# describe() -> gera estatísticas
print(
  '\n===Estátisticas (quantidade, média, mínimo, máximo, etc)===\n', 
  df.describe()
)

# shape -> tamanho da base. usa uma vetor/tupla: (linhas, colunas)
# print(df.shape)

print('\n===Tamanho da tabela===')
print('* Quantidade de linhas:', df.shape[0])
print('* Quantidade de colunas:', df.shape[1])

# renomeando o nome das colunas da tabela

# foi criado um "dicionário" que referencia as colunas antigas 
# e diz qual deve ser o novo nome para cada uma delas
colunas_traduzidas = {
  'work_year': 'ano',
  'experience_level': 'experiencia',
  'employment_type': 'tipo_emprego',
  'job_title': 'cargo',
  'salary': 'salario',
  'salary_currency': 'moeda',
  'salary_in_usd': 'salario_usd',
  'employee_residence': 'residencia',
  'remote_ratio': 'taxa_remoto',
  'company_location': 'local_empresa',
  'company_size': 'tamanho_empresa'
}

# rename() -> aplicar a renomeação. 

# inplace -> define se deve criar uma cópia (inplace=False) 
# ou se deve modificar a tabela original (inplace=True)
# por padrão: se não definir nada, o inplace é igual à False

df.rename(columns=colunas_traduzidas, inplace=True)

print(
  '\n===Nome das colunas traduzidas===\n', 
  df. columns
)

# value_counts() -> contar quantas vezes determinado(s) valor(es) aparece(m) na tabela
# nesse caso foi filtrado para contar somente os valores da coluna 'experiencia'
print(
  '\n===Contagem de experiência===\n',
  df['experiencia'].value_counts()
)