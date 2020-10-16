from django.db import models
import pandas as pd

from patic.core.models import moeda

def ficha_avaliacao_context(docfile):
    
    nome = docfile.name[:-5]
    frame = raw_dataset(docfile)    
    acoes = [{
        'nome': row['acao'],
        'unidade': row['unidade'],
        'objeto': row['objeto'],
        'contrato_novo_ou_renovacao': row['contrato_novo_ou_renovacao'],
        'quantidade': row['quantidade'],
        'valor': f"R$ {moeda(row['valor'])}"
        } for index, row in frame.iterrows()]

    return {'acoes': acoes, 'nome':nome}

def raw_dataset(file):
    
    df = pd.ExcelFile(file)
    df = df.parse("Planejamento")
    df = df.iloc[7:]
    df = df.iloc[:, :9]
    df.columns = ['unidade', 'acao', 'justificativa', 'especificacao_do_item', 'objeto', 
                  'duracao', 'contrato_novo_ou_renovacao', 'quantidade', 'valor']
    df = df.dropna(subset=['acao'])
    df = df.where(pd.notnull(df), None)
    df = df.reset_index(drop=True)
    return df