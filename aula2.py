import pandas as pd
from numpy import nan
from dataframes import traduzir_df

df = traduzir_df()

# isnull() -> traz uma tabela de booleano
# especificando se os valores são nulos ou não
print(
  df.isnull()
)

# contando quantos nulos existem
print(
  df.isnull().sum()
)

print(
  df.columns[df.isnull().any(axis=0)]
)

# unique() -> vetor dos valores únicos ("individuais") 
print(
  df['ano'].unique()
)

'''
fazendo um filtro...
tá pegando só as linhas onde os valores são nulos (True na tabela do isnull())
axis = eixo... basicamente horizontal (1) ou vertical (0) OU linha à linha / coluna a coluna
-> por padrão, axis = 0
aq tem que ser horizontal pq esse padrão ( df[...] ) aceita apenas filtro de linha...
'''
print(
  df[df.isnull().any(axis=1)]
)

'''
# exemplo para usar axios=0

print(
  df.columns[df.isnull().any()] # por padrão o axis é sempre 0
)
-> mostra o nome das colunas q tem pelo menos um valor null

obviamente o df.columns só aceita filtro de coluna,
por isso tem que usar o eixo vertical/de coluna (axis=0)
'''

# criando um df do zero
df_salarios = pd.DataFrame({
  'nome': [
    'Maya', 'Sam', 'Lotus', 'Mikki'
  ],
  
  'salario': [
    7000, nan, 18500, 200
  ]
})

'''
# preechendo os valores null com a media

fillna() -> preencher os nulos com algum valor

os nulos serão preenchidos com a média dos salários ( df['salario'].mean() )
arredondado com duas casas decimais ( round(2) )

isso vai ser aplicado numa coluna nova (fill_media),
só por questão de didática (comparar as alterações)
'''

df_salarios['fill_media'] = (
  df_salarios['salario']
  .fillna(
    df_salarios['salario']
    .mean().round(2)
  )
)

# agora a mediana (median) sem arredondar
df_salarios['fill_mediana'] = (
  df_salarios['salario']
  .fillna(
    df_salarios['salario']
    .median()
  )
)

print(df_salarios)

df_temperaturas = pd.DataFrame({
  'dia' : [
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta'
  ],

  'temperatura': [
    30, nan, nan, 20, 27
  ]
})

# ffill() -> "forward fill". coloca nos nulos o valor-não-nulo anterior
# é pq ele vai da linha 0 até o final...
df_temperaturas['ffill'] = (
  df_temperaturas['temperatura']
  .ffill()
)

# bfill() -> "backward fill". coloca nos nulos o valor-não-nulo *posterior*
# é pq ele vai do final até 0...
df_temperaturas['bfill'] = (
  df_temperaturas['temperatura']
  .bfill()
)

print(df_temperaturas)

df_cidades = pd.DataFrame({
  'nome': [
    'Maya', 'Sam', 'Lotus', 'Mikki'
  ],

  'cidade': [
    'Lá', 'Ali', nan, 'Onde Judas perdeu as botas'
  ] 
})

df_cidades['fillna'] = (
  df_cidades['cidade']
  .fillna('Nao informado')
)

print(df_cidades)

# dropna() -> dropar as linhas que possuem nulo em qualquer coluna
df_limpo = df.dropna()

# provando que não há mais nulos
print(
  df_limpo.isnull().sum()
)

'''
# esse código vai retornar um dt vazio (pq n tem mais nulos)
print(
  df_limpo[df_limpo.isnull().any(axis=1)]
)
'''

# trocando dtype da coluna ano
# assign() -> adicionar/tratar colunas
# astype() -> atribuir tipo
df_limpo = df_limpo.assign(
  ano = ( # selecionei a coluna ano
    df_limpo['ano']
    .astype('int64')
  )
)

df_limpo.info()
