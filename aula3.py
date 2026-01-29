import pandas as pd
from dataframes import limpar_df
import matplotlib.pyplot as plt # lib para exibir os gráficos
import seaborn as sns # lib para fazer gráfico personalizados
import plotly.express as px # lib para fazer gráficos interativos

df_limpo = limpar_df()

# figure() -> certifica que uma figura será criada
plt.figure()
# e a próxima linha é o que vai ser inserido na figura
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de senioridade')

plt.figure()
df_limpo['ano'].value_counts().plot(kind='bar', title='Anos')

# fznd agrupamentos no pandas
ordem = (
  df_limpo.groupby(
    'senioridade' # coluna que será agrupada
  )['salario_usd'].mean().sort_values(ascending=False)
).index
'''
agrupando por senioridade,
gerar estatísticas em cima do salario, 
calcular média
e ordenar do maior pro menor (ascending=False -> crescente=Falso)
index -> objeto que contém a lista ordenada da senioridade
'''

# figsize -> tamanho da figura
# usa uma tupla: (largura, altura)
plt.figure(figsize=(8,5))
# barplot() -> gráfico de barras
sns.barplot(
  data=df_limpo, # base de dados que será usada
  x='senioridade', # eixo horizontal usa a coluna senioridade
  y='salario_usd', # o eixo vertical usa a salario_usd
  order=ordem # definindo a ordem
)
plt.title('Salário médio anual por nível de senioridade')
# xlabel() e ylabel() -> definir título (ou rótulo) do eixo
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (USD)')

# histplot() -> histograma (freq com q um valor aparece)
plt.figure(figsize=(8,4))
sns.histplot(
  data=df_limpo['salario_usd'],
  bins=50, # intervalo entre as barras
  kde=True # linha que segue as barras
)
plt.title('Distruição do salário anual em dólares')
plt.xlabel('Salário (USD)')
plt.ylabel('Frequência')

# boxplot() -> gráfico de distruibuição em caixas
plt.figure(figsize=(8,5))
sns.boxplot(
  x=df_limpo['salario_usd']
)
plt.title('Frequência salarial em dólares')
plt.xlabel('Salário (USD)')

plt.figure(figsize=(8,5))
sns.boxplot(
  data=df_limpo,
  x='senioridade',
  y='salario_usd',
  order=['Junior', 'Pleno', 'Senior', 'Executivo'],
  palette='Set2',
  hue='senioridade' # em qual categoria a paleta vai operar
)
plt.title('Distruição salarial por senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário (USD)')

# variável para a ordem do gráfico interativo
ordem_interativo = (
  df_limpo.groupby(
    'senioridade' # coluna que será agrupada
  )['salario_usd'].mean().sort_values(ascending=False)
).reset_index()

# variável para armazenar o gráfico interativo
fig_bar = px.bar(
  data_frame=ordem_interativo,
  x='senioridade',
  y='salario_usd',
  title='Média salarial por senioridade',
  labels={ # labels é um dicionário. especifica a coluna que quero trocar o nome
    'salario_usd': 'Média salarial anual (USD)'
  }
)
fig_bar.show()

fig_pizza = px.pie(
  data_frame=df_limpo['remoto'].value_counts().reset_index(),
  title='Proporção dos tipos de trabalho',
  names='remoto', # categorias ou pedaços da pizza
  values='count', # definindo os valores
  labels={
    'remoto': 'Tipo de trabalho',
    'count': 'Quantidade'
  },
  hole=0.3 # tamanho do buraco. pra fazer uma rosquinha 
)
# exibir as labels e a % fora dos pedaços 
fig_pizza.update_traces(textinfo='percent+label')
fig_pizza.show()

# plt.show() -> vai mostrar todas as figuras criadas em janelas separadas
plt.show()
