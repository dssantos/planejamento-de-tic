from django.db import models
import pandas as pd


def ficha_avaliacao_context(docfile):
    
    nome = docfile.name[:-5]
    frame = raw_dataset(docfile)
    hardwares = [{
        'nome': row['acao'],
        'valor': row['valor'],
        'quantidade': row['quantidade'],
        'indicacao_comite': 'Não'
        } for index, row in frame.iterrows() if row['objeto'] == 'Hardware']
    softwares = [{
        'nome': row['acao'],
        'valor': row['valor'],
        'quantidade': row['quantidade'],
        'indicacao_comite': 'Não'
        } for index, row in frame.iterrows() if row['objeto'] == 'Software']
    servicos = [{
        'nome': row['acao'],
        'valor': row['valor'],
        'comum_ou_nao_comum': row['objeto'],
        'renovacao_de_contrato': row['contrato_novo_ou_renovacao'],
        'indicacao_comite': 'Não'
        } for index, row in frame.iterrows() if row['objeto'] in ['Serviço Comum', 'Serviço Não Comum']]
    servicos_prod = [{
        'nome': row['acao'],
        'valor': row['valor'],
        'obrigatorio_ou_nao_obrigatorio': row['objeto'],
        'renovacao_de_contrato': row['contrato_novo_ou_renovacao'],
        'indicacao_comite': 'Não'
        } for index, row in frame.iterrows() if row['objeto'] in ['Prodeb Obrigatório', 'Prodeb Não Obrigatório']]
    
    return {'hardwares': hardwares, 'softwares': softwares, 
            'servicos': servicos, 'servicos_prod': servicos_prod, 'nome':nome, 'frame': frame}

def raw_dataset(file):
    
    df = pd.ExcelFile(file)
    df = df.parse("Planejamento")
    df = df.iloc[7:]
    df = df.iloc[:, :9]
    df.columns = ['unidade', 'acao', 'justificativa', 'especificacao_do_item', 'objeto', 
                  'duracao', 'contrato_novo_ou_renovacao', 'quantidade', 'valor']
    df = df.dropna(subset=['acao'])
    df = df.reset_index(drop=True)
    return df