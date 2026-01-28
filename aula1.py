import pandas as pd

# df = dataframe (tabela)
df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

# head(X) -> mostrar as X primeiras linhas da tabela
print(
  '===Primeiras 10 linhas da tabela===\n',
  df.head(10)
)

# info() -> parecido com o DESC do sql
print('\n===Informações===')
df.info()

# describe() -> gera estatísticas
print(
  '\n===Estátisticas (quantidade, média, mínimo, máximo, etc)===\n', 
  df.describe()
)

# shape -> tamanho da base. usa uma vetor/tupla: (linhas, colunas)

print('''
===Tamanho da tabela===
* Quantidade de linhas: {}
* Quantidade de colunas: {}
'''
.format(df.shape[0], df.shape[1])
)

# rename() -> aplicar renomeação das colunas 

# inplace -> define se deve criar uma cópia (inplace=False) 
# ou se deve modificar a tabela original (inplace=True)
# por padrão é igual à False

df.rename(columns={
  'work_year': 'ano',
  'experience_level': 'senioridade',
  'employment_type': 'contrato',
  'job_title': 'cargo',
  'salary': 'salario',
  'salary_currency': 'moeda',
  'salary_in_usd': 'salario_usd',
  'employee_residence': 'residencia',
  'remote_ratio': 'remoto',
  'company_location': 'local_empresa',
  'company_size': 'tamanho_empresa'
}, inplace=True)

print(
  '===Nome das colunas traduzidas===\n', 
  df.columns
)

# replace() -> alterar os valores de uma coluna específica. tbm possui implace
df['senioridade'] = df['senioridade'].replace({
  'SE': 'Senior',
  'MI': 'Pleno',
  'EN': 'Junior',
  'EX': 'Executivo'
})

df['contrato'] = df['contrato'].replace({
  'FT': 'Integral',
  'PT': 'Meio periodo',
  'FL': 'Freelancer',
  'CT': 'Temporario'
})

df['tamanho_empresa'] = df['tamanho_empresa'].replace({
  'L': 'Grande',
  'M': 'Media',
  'S': 'Pequena',
})

# aq usei map só pq n tava aparecendo nas estatística finais
df['remoto'] = df['remoto'].map({
  100: 'Remoto',
  50: 'Hibrido',
  0: 'Presencial'
})

# value_counts() -> contar quantas vezes determinado(s) valor(es) aparece(m) na tabela
# nesse caso foi filtrado para contar somente os valores da coluna 'senioridade'
print(
  '\n===Contagem de experiência===\n',
  df['senioridade'].value_counts()
)

print(
  '\n===Contagem dos contratos===\n',
  df['contrato'].value_counts()
)

print(
  '\n===Contagem de experiência===\n',
  df['tamanho_empresa'].value_counts()
)
print(
  '\n===Contagem da taxa de remoto===\n',
  df['remoto'].value_counts()
)

print(
  '\n===Primeira 5 linhas pós-alterações===\n',
  df.head()
)

# include='object' -> vai trazer tbm valores de string (considerados "objects" para o Pandas)
# na vdd agr é considerado obsoleto... blz ne?
print(
  '\n===Estatísicas das colunas dtype=\'str\'===\n',
  df.describe(include='str')
)