from django.db import models

import os, re
import pandas as pd

import locale

from decouple import config


def filelist():

    pasta_acao = config('PASTA_ACAO', default=".\contrib\plan")   # Formato Unix

    files = []

    for r, d, f in os.walk(pasta_acao):
        for file in f:
            if ('.xlsx' in file) and ('~$' not in file):
                files.append(os.path.join(r, file))

    return files


def filepath():
    return filelist()[0]


def dadospa():
    xl = pd.ExcelFile(filepath())
    df = xl.parse("Planejamento")
    df = df.drop(columns=['Unnamed: 9', 'Unnamed: 10'])
    df = df.iloc[6:]
    df = df.dropna(subset=['Unnamed: 1'])
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    return df


def moeda(v):
    valor = clearnumber(v)
    locale.setlocale(locale.LC_ALL, '')
    valor = locale.currency(valor, grouping=True, symbol=None)
    return valor

def clearnumber(n):
    # Remove caracteres indesejados
    n = re.sub('[^0-9\.].', '', str(n))
    return float(n)