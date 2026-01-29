from pandas import read_csv

df = read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

def traduzir_df():
  df_traduzido = df

  df_traduzido.rename(columns={
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


  # replace() -> alterar os valores de uma coluna específica. tbm possui implace
  df_traduzido['senioridade'] = df_traduzido['senioridade'].replace({
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
  })

  df_traduzido['contrato'] = df_traduzido['contrato'].replace({
    'FT': 'Integral',
    'PT': 'Meio periodo',
    'FL': 'Freelancer',
    'CT': 'Temporario'
  })

  df_traduzido['tamanho_empresa'] = df_traduzido['tamanho_empresa'].replace({
    'L': 'Grande',
    'M': 'Media',
    'S': 'Pequena',
  })

  # aq usei map só pq n tava aparecendo nas estatística finais
  df_traduzido['remoto'] = df_traduzido['remoto'].map({
    100: 'Remoto',
    50: 'Hibrido',
    0: 'Presencial'
  })

  return df_traduzido

def limpar_df():
  df_limpo = traduzir_df().dropna()
    
  df_limpo = df_limpo.assign(
    ano = ( 
      df_limpo['ano']
      .astype('int64')
    )
  )
  
  return df_limpo
