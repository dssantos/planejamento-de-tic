from django.db import models

from django.db import models
import pandas as pd

from patic.core.models import moeda


def convert_binary_xls_acoes_to_frame(binary_xls):
    
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
