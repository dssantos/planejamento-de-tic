from django.db import models

import os, re
import pandas as pd

import locale

from decouple import config


def filelist():

    pasta_exec = config('PASTA_EXEC', default="./contrib/exec")   # Formato Unix

    files = []

    for r, d, f in os.walk(pasta_exec):
        for file in f:
            if ('.xlsx' in file) and ('~$' not in file):
                files.append(os.path.join(r, file))

    return files


def filepath():
    return filelist()[0]


def dadospa():
    xl = pd.ExcelFile(filepath())
    df = xl.parse("Execução")
    df = df.drop(columns=['Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22'])
    df = df.iloc[6:]
    df = df.dropna(subset=['Unnamed: 2'])
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