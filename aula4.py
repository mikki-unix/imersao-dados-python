import streamlit as st # lib para criar uma página web com dashboards
import pandas as pd
import plotly.express as px

st.set_page_config(
  page_title='Dashboard de salários na área de dados', # <title>
  page_icon='📊', # favicon
  layout='wide'
)


df = pd.read_csv('https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv')

# sidebar -> definir uma sidebar para a página
st.sidebar.header('Filtros')

# sorted() -> método do python para ordenar uma lista em ordem crescente
anos_disponiveis = sorted(df['ano'].unique())
# multiselect() -> criar uma seletor múltiplo
anos_selecionados = st.sidebar.multiselect(
  label='Ano',
  options=anos_disponiveis, # opções para escolher
  default=anos_disponiveis # opções já habilitadas/escolhidas
)

senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect(
  label='Senrioridade',
  options=senioridades_disponiveis,
  default=senioridades_disponiveis
)

contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect(
  label='Tipo de contrato',
  options=contratos_disponiveis,
  default=contratos_disponiveis
)

tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect(
  label='Tamanho da empresa',
  options=tamanhos_disponiveis,
  default=tamanhos_disponiveis
)

# criando df filtrado com condições
df_filtrado = df[
  # somente as linhas que estão entre (isin) os anos selecionados (o multiselect criado)
  (df['ano'].isin(anos_selecionados)) &
  (df['senioridade'].isin(senioridades_selecionadas)) &
  (df['contrato'].isin(contratos_selecionados)) &
  (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# title() -> <h1> / é maior que o # do md
st.title('📊 Dashboard de salários na área de dados')
# markdown() -> literalmente usa md para criar elementos na página
st.markdown('Explore **insights atuais** sobre a área de dados. Use os **filtros** à esquerda para refinir sua análise')

# empty -> é um booleano
if not df_filtrado.empty: 
  salario_medio = df_filtrado['usd'].mean()
  salario_maximo = df_filtrado['usd'].max()
  total_registros = df_filtrado.shape[0]

  # mode() -> uma tabela com o(s) valor(es) mais frequente(s)
  # o indíce zero é só pra pegar o texto ao invés da tabela
  cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
  salario_medio,
  salario_maximo,
  total_registros,
  cargo_mais_frequente = 0, 0, 0, ''

# columns(n) -> cria uma seção com n divisões
col1, col2, col3, col4 = st.columns(4)
# metric() -> um tipo de card
col1.metric('Salário médio', f'${salario_medio:,.0f}')
col2.metric('Salário máximo', f'${salario_maximo:,.0f}')
col3.metric('Total de registros', f'{total_registros:,}')
col4.metric('Cargo mais frequente', cargo_mais_frequente)

st.markdown('---')

# subheader() -> <h2>
st.subheader('Gráficos')

col_graf1, col_graf2 = st.columns(2)

# with -> simplifica try/catch
with col_graf1:
  if not df_filtrado.empty:
    top_cargos = (
      df_filtrado.groupby('cargo')['usd']
      .mean()
      .nlargest(10) # os n maiores
      .sort_values(ascending=True)
      .reset_index()
    )

    grafico_cargos = px.bar(
      top_cargos,
      x='usd',
      y='cargo',
      orientation='h', # vai deixar as barras na horizontal
      title='Top 10 cargos por salário médio',
      labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
    )
    
    # grafico_cargos.update_layout(yaxis={'categoryorder':'total ascending'})
    # -> código redudante. o que isso faz é ordenar do maior pro menor (coisa que já foi feita no agrupamento)
    st.plotly_chart(grafico_cargos, width='stretch')

  else:
    st.warning('Nenhum dado para exibir no gráfico de cargos.')

with col_graf2:
  if not df_filtrado.empty:
    grafico_hist = px.histogram(
      df_filtrado,
      x='usd',
      nbins=30,
      title='Distribuição de salários anuais',
      labels={'usd': 'Faixa salarial (USD)', 'count': ''}
    )
    st.plotly_chart(grafico_hist, width='stretch')

  else:
    st.warning('Nenhum dado para exibir no gráfico de distribuição.')

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
  if not df_filtrado.empty:
    grafico_remoto = px.pie(
      df_filtrado['remoto'].value_counts().reset_index(),
      names='remoto',
      values='count',
      title='Proporção dos tipos de trabalho',
      hole=0.5,
      labels={
        'remoto': 'Tipo de trabalho',
        'count': 'Quantidade'
      }
    )
    grafico_remoto.update_traces(textinfo='percent+label')
    st.plotly_chart(grafico_remoto, width='stretch')
  else:
    st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
  if not df_filtrado.empty:
    media_ds_pais = (
      df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
      .groupby('residencia_iso3')['usd'].mean().reset_index()
    )
    grafico_paises = px.choropleth(
      media_ds_pais,
      locations='residencia_iso3',
      color='usd',
      color_continuous_scale='rdylgn',
      title='Salário médio de Cientista de Dados por país',
      labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
    )
    st.plotly_chart(grafico_paises, width='stretch')
  else:
    st.warning("Nenhum dado para exibir no gráfico de países.") 

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)
