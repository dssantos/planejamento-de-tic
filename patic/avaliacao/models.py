from django.db import models

def ficha_avaliacao_context(docfile):

    hardwares = [
        {
        'nome': 'acao1',
        'valor': 'R$ 1.00',
        'quantidade': '1',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao2',
        'valor': 'R$ 2.00',
        'quantidade': '2',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao3',
        'valor': 'R$ 300000.00',
        'quantidade': '1',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao4',
        'valor': 'R$ 42265488488.00',
        'quantidade': '2',
        'indicacao_comite': 'Não'
        },
    ]
    softwares = [
        {
        'nome': 'acao1',
        'valor': 'R$ 1.00',
        'quantidade': '1',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao2',
        'valor': 'R$ 2.00',
        'quantidade': '2',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao3',
        'valor': 'R$ 300000.00',
        'quantidade': '1',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao4',
        'valor': 'R$ 42265488488.00',
        'quantidade': '2',
        'indicacao_comite': 'Não'
        },
    ]
    servicos = [
        {
        'nome': 'acao1',
        'valor': 'R$ 1.00',
        'comum_ou_nao_comum': 'Comum',
        'renovacao_de_contrato': 'Não',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao2',
        'valor': 'R$ 2.00',
        'comum_ou_nao_comum': 'Comum',
        'renovacao_de_contrato': 'Não',
        'indicacao_comite': 'Não'
        },
    ]
    servicos_prod = [
        {
        'nome': 'acao1',
        'valor': 'R$ 1.00',
        'obrigatorio_ou_nao_obrigatorio': 'Não Obrigatório',
        'renovacao_de_contrato': 'Não',
        'indicacao_comite': 'Não'
        },
        {
        'nome': 'acao2',
        'valor': 'R$ 2.00',
        'obrigatorio_ou_nao_obrigatorio': 'Obrigatório',
        'renovacao_de_contrato': 'Não',
        'indicacao_comite': 'Não'
        },
    ]
    
    return {'hardwares': hardwares, 'softwares': softwares, 'servicos': servicos, 'servicos_prod': servicos_prod}
