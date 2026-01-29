import pandas as pd
from dataframes import traduzir_df
import matplotlib.pyplot as plt # lib para exibir os gráficos
import seaborn as sns # lib para fazer gráfico personalizados

df = traduzir_df()

print(
  df[df['cargo'] == 'Data Scientist']
)

plt.figure()
sns.barplot(
  data=df[df['cargo'] == 'Data Scientist'], 
  x='local_empresa',
  y='salario_usd',
)
plt.title('Distrição de salário (USD) por país para o cargo de Cientista de Dados')
plt.xlabel('país')

plt.figure()
sns.barplot(
  data=df, 
  x='local_empresa',
  y='salario_usd',
)
plt.title('Distrição de salário (USD) por país')
plt.xlabel('país')

plt.show()