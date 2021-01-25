import sys

from django.db import models
import pandas as pd

from patic.core.models import moeda


def convert_binary_xls_configs_to_dataframe(binary_xls):
    configs = pd.read_excel(binary_xls, sheet_name='Config')
    return configs 

def convert_binary_xls_acoes_to_dataframe(binary_xls):
    
    df = pd.ExcelFile(binary_xls)
    df = df.parse("Planejamento") # Planilha de ações
    df = df.iloc[7:]
    df = df.iloc[:, :9]
    df.columns = ['unidade', 'acao', 'justificativa', 'especificacao_do_item', 'objeto', 
                  'duracao', 'contrato_novo_ou_renovacao', 'quantidade', 'valor']
    df = df.dropna(subset=['acao'])
    df = df.where(pd.notnull(df), None)
    df = df.reset_index(drop=True)
    return df

def check_actions_sheet_errors(binary_xls):
    import os
    import numpy as np

    configs_dataframe = convert_binary_xls_configs_to_dataframe(binary_xls)
    actions_dataframe = convert_binary_xls_acoes_to_dataframe(binary_xls)
    
    try:
        especificacoes = configs_dataframe['Especificação do Item'].dropna().tolist()
        objetos = configs_dataframe['Objeto da aquisição'].dropna().tolist()
        contratos = configs_dataframe['Contrato'].dropna().tolist()

    except ValueError as err:
        return pd.DataFrame({'Erro':['A estrutura da Planilha está diferente do modelo padrão.'], 'Detalhes':[err]})
    except:
        return pd.DataFrame({'Erro':['Ocorreu um erro inesperado.'], 'Detalhes':[sys.exc_info()[:]]})

    linhas = []
    acoes = []
    erros = []
    vazio = 0
    rows = actions_dataframe.reset_index().iterrows()
    for index, row in rows:
        linha = row['index']+9
        acao = row['acao']
        justificativa = row['justificativa']
        especificacao = row['especificacao_do_item']
        objeto = row['objeto']
        duracao = row['duracao']
        contrato = row['contrato_novo_ou_renovacao']
        quantidade = row['quantidade']
        valor = row['valor']

        if pd.isna(justificativa):
            vazio += 1

        if pd.isna(especificacao):
            vazio += 1
        elif especificacao not in especificacoes:
            acoes.append(acao)
            erros.append(f'Especificação do Item inválida: "{especificacao}"')
            linhas.append(linha)

        if pd.isna(objeto):
            vazio += 1
        elif objeto not in objetos:
            acoes.append(acao)
            erros.append(f'Objeto da aquisição inválido: "{objeto}"')
            linhas.append(linha)
                
        if pd.isna(duracao):
            vazio += 1
        elif not isinstance(duracao, (int, float)):
            acoes.append(acao)
            erros.append(f'Duracao inválida: "{duracao}", Tipo: {type(duracao).__name__}')
            linhas.append(linha)

        if pd.isna(contrato):
            vazio += 1
        elif contrato not in contratos:
            acoes.append(acao)
            erros.append(f'Contrato inválida: "{contrato}"')
            linhas.append(linha)

        if pd.isna(quantidade):
            vazio += 1
        elif not isinstance(quantidade, (int, float)):
            acoes.append(acao)
            erros.append(f'Quantidade inválida: "{quantidade}", Tipo: {type(quantidade).__name__}')
            linhas.append(linha)

        if pd.isna(valor):
            vazio += 1
        elif not isinstance(valor, (int, float)):
            acoes.append(acao)
            erros.append(f'Valor inválido: "{valor}", Tipo: {type(valor).__name__}')
            linhas.append(linha)
                    
        if vazio > 0:
            acoes.append(acao)
            erros.append(f'Campos vazios: {vazio}')
            vazio = 0
            linhas.append(linha)
            
    return pd.DataFrame({'Linha da Planilha':linhas, 'Ação': acoes, 'Erro': erros})