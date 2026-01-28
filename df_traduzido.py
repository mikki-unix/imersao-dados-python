from pandas import read_csv

def importar_traduzir_df():
  df = read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

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

  return df
